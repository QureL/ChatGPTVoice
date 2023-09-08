from ui.design.Ui_gpt_main_window import Ui_gpt_chat_widget
from ui.gui_gpt_session import GPTSessionSelect
from PySide6.QtWidgets import QWidget

from const import *
from gpt import gpt
import logging, sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
from config.config import GPTChatConfig
from config.const import *

from processor.processor import S2TLocalServer, Text2SpeechProccessor, ResultCorrectPipeline, GPT2T2SProcessorPipeline
from PySide6.QtCore import Signal


class GPTWidget(QWidget, Ui_gpt_chat_widget):

    text_browser_signal = Signal(str)
    correct_s2t_editor_signal = Signal(str)
    shall_correct_s2t = False

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.mode = Mode.MODE_CHAT

        self.gpt_session_select_window = GPTSessionSelect(parent=self)
        self.config = GPTChatConfig()

        self.initial()
        self.render_combo_boxes()
        self.bind_buttons_chat()

    def initial(self):
        self._initial_proceesor_recorder_speaker()
        self._initial_gpt_bridge()
    
    def _initial_gpt_base_key(self):
        import openai
        openai.api_base = self.config.get_config(OPENAI_API_BASE)
        openai.api_key = self.config.get_config(OPENAI_API_KEY)

    def _initial_signals(self): # called when initialing intercepts
        self.correct_s2t_editor_signal.connect(self.tab1_correct_s2t_editor.appendPlainText)

        def text_browser_signal_callback(txt:str):
            txt = "[GPT]" + txt
            txt = "<font color=\"#FF0000\">" + txt + "</font>"

            self.textBrowser.append(txt)
        
        self.text_browser_signal.connect(text_browser_signal_callback)

    def _initial_proceesor_recorder_speaker(self):
        self._initial_signals()    
        from audio import audio
        from audio.speaker_windows import SpeakderPyTTSx3

        speed = self.config.get_config(GPT_SPEAK_SPEED)
        self.audio_keeper = audio.AudioDeviceKeepr()
        # self.speaker = audio.AudioSpeaker(keeper=self.audio_keeper, speed=speed)
        self.speaker = SpeakderPyTTSx3(speed=int(speed)/10)
    
        self.correct_s2t_pipe = ResultCorrectPipeline(self.correct_s2t_editor_signal, None)


        self.s2t_proccssor = S2TLocalServer(ws_address=config['S2T_PROCESSOR_ADDRESS'],
                                                    output_pipe=self.correct_s2t_pipe)
        
        self.t2s_processor = Text2SpeechProccessor(ws_address=config['T2S_PROCESSOR_ADDRESS'],
                                                   output_pipe=self.speaker) # TODO
        
        self.gpt_to_t2s_pipe = GPT2T2SProcessorPipeline(self.text_browser_signal, self.speaker)

        self.recorder = audio.AudioRecorder(
            keeper=self.audio_keeper,
            output_pipe=self.s2t_proccssor,
            is_chat=self.mode == Mode.CHAT,
            secs=6
        )
        

    def _initial_gpt_bridge(self):
        URL = config['gpt']['url']
        TOKEN = config['gpt']['token']
        requestor = gpt.GPTReuqestor(token=TOKEN, url=URL, context_cnt=config['gpt']['context_cnt'])
        requestor.set_system_command(config['gpt']['preset'])
        self.requstor = requestor

        self.gpt_bridge = gpt.ConcurrentGPTBridge(
            gpt_requestor=requestor,
            output_pipe=self.gpt_to_t2s_pipe)
        
    def start(self):
        self._select_audio_device()
        # start recorder and speaker 
        self.recorder.start_timer() # timer couldn`t start from child thread
        self.speaker.start()
        self.recorder.start()
        logging.debug("speaker and recorder start...")

        # start t2s and s2t
        self.s2t_proccssor.start()
        #self.t2s_processor.start()
        self.gpt_bridge.start()
        logging.debug("processor start...")


    def render_combo_boxes(self):
        devices = self.audio_keeper.display_devices()
        combo_boxes = [
            self.tab1_select_input_combo, # self.tab1_select_outpt_combo
        ]
        for box in combo_boxes:
            box.addItems(devices)
        
        self.tab1_select_outpt_combo.addItems(self.speaker.show_voices())

    def _select_audio_device(self):
        self.recorder.select_device(
            self.tab1_select_input_combo.currentText())
        
        #self.speaker.select_device(self.tab1_select_outpt_combo.currentText())
        self.speaker.select_voice(self.tab1_select_outpt_combo.currentText())



    def bind_buttons_chat(self):
        self._state = "idle"
        stop_text, start_text = "停止说话", "开始说话"
        change_text = self.tab1_start_btn.setText
        switch = self.recorder.switch

        def chat_start():
            if self._state == "idle":

                self.start()
                change_text(stop_text)
                self._state = "recording"
            elif self._state == "recording":
                switch()
                self._state = "stopping"
                change_text(start_text)
            else:
                switch()
                self._state = "recording"
                change_text(stop_text)

        self.tab1_start_btn.clicked.connect(chat_start)

        def tab1_select_correct_s2t_combo_callback():
            index = self.tab1_select_correct_s2t_combo.currentIndex()
            self.shall_correct_s2t = False if index == 0 else True
            logging.debug("correct s2t result=%s", self.tab1_select_correct_s2t_combo.currentText())
        
        self.tab1_select_correct_s2t_combo.currentIndexChanged.connect(
            tab1_select_correct_s2t_combo_callback)

        def tab1_send_corrected_text_btn_callback():
            if not self.shall_correct_s2t: return
            txt = self.tab1_correct_s2t_editor.toPlainText()
            if len(txt) == 0: return
            self.gpt_bridge.put(txt)
            self.tab1_correct_s2t_editor.clear()
            txt = "<font color=\"#00FF00\">" + "[Human]" + txt + "</font>"
            self.textBrowser.append(txt)


        
        self.tab1_send_corrected_text_btn.clicked.connect(tab1_send_corrected_text_btn_callback)
        def tab1_pause_speaker_btn_callback():
            self.speaker.pause()
            if self.tab1_pause_speaker_btn.text() == '暂停':
                self.tab1_pause_speaker_btn.setText('继续')
            else:
                self.tab1_pause_speaker_btn.setText('暂停')

        self.tab1_pause_speaker_btn.clicked.connect(tab1_pause_speaker_btn_callback)

        self.tab1_load_session_btn.clicked.connect(self.gpt_session_select_window.show)

        self.tab1_speak_again_btn.clicked.connect(self.speaker.speak_again)


    def release_resource(self):
        self.recorder.terminate()
        self.speaker.terminate()
        #self.t2s_processor.terminate()
        self.s2t_proccssor.terminate()
        self.gpt_bridge.terminate()


    def set_session(self, session_name):
        logging.info("SetSession, %s", session_name)
        self.requstor.set_session(session_name)

