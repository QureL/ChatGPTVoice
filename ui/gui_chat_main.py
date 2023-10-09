# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. 
# If a copy of the MPL was not distributed with this file, 
# You can obtain one at https://mozilla.org/MPL/2.0/.
#
# Author: qurel
# GitHub: https://github.com/QureL/horn
# Copyright reserved

from ui.design.Ui_gpt_main_window import Ui_gpt_chat_widget
from ui.gui_gpt_session import GPTSessionSelect
from PySide6.QtWidgets import QWidget

from const import *
import logging, sys
from ui.gui_chat_setting import GPTSettingWindow
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
from config.const import *

from PySide6.QtCore import Signal
from controller.gpt_chat_controller import GPTChatController
from ui.custom.voice_control_button import VoiceControlButton
from config.config_json import dump_config

class GPTWidget(QWidget, Ui_gpt_chat_widget):

    text_browser_signal = Signal(str)
    correct_s2t_editor_signal = Signal(str)
    shall_correct_s2t = False

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.mode = Mode.MODE_CHAT
        
        self.gpt_session_select_window = GPTSessionSelect(parent=self)
        self.gpt_setting_window = GPTSettingWindow(self)

        self.controller = GPTChatController.get_instance()
        self.render_ui()
        self.render_combo_boxes()
        self.bind_buttons()
        self.bind_signals()
        self.bind_controller_callback()

    # 画禁声按钮
    def render_ui(self):
        self.voice_control_button = VoiceControlButton(self)
        self.verticalLayout.insertWidget(0, self.voice_control_button)


    def render_combo_boxes(self):
        self.tab1_select_input_combo.addItems(self.controller.display_audio_input_devices())
        self.tab1_select_outpt_combo.addItems(self.controller.display_audio_voices())

    def bind_buttons(self):
        #################################
        def start_btn_clicked_callback():
            self.update_configurations()
            # todo: to be graceful
            self.controller.record_or_pause()
            if self.tab1_start_btn.text() == "Talk":
                self.tab1_start_btn.setText('Stop')
            else:
                self.tab1_start_btn.setText('Talk')
        self.tab1_start_btn.clicked.connect(start_btn_clicked_callback)
        #################################
        def tab1_send_corrected_text_btn_callback():
            txt = self.tab1_correct_s2t_editor.toPlainText()
            if len(txt) == 0: return
            self.controller.input_human_message(txt)

            self.tab1_correct_s2t_editor.clear()
            txt = "<font color=\"#00FF00\">" + "[Human]" + txt + "</font>"
            self.textBrowser.append(txt)
        self.tab1_send_corrected_text_btn.clicked.connect(tab1_send_corrected_text_btn_callback)

        #################################
        def voice_control_btn_callback():
            self.controller.pause_speaking()
            self.voice_control_button.re_paint()

        self.voice_control_button.clicked.connect(voice_control_btn_callback)
        self.tab1_load_session_btn.clicked.connect(self.gpt_session_select_window.show)

        def btn_gpt_setting_callback():
            self.gpt_setting_window.render_ui()
            self.gpt_setting_window.show()
        self.btn_gpt_setting.clicked.connect(btn_gpt_setting_callback)

    # 配置speaker声音，recorder输入设备
    def update_configurations(self):
        input_device = self.tab1_select_input_combo.currentText()
        output_voice = self.tab1_select_outpt_combo.currentText()

        self.controller.set_attributes_speaker(speaker_voice=output_voice)
        self.controller.set_attributes_recorder(recorder_input_device=input_device)

    def bind_signals(self):
        self.correct_s2t_editor_signal.connect(self.tab1_correct_s2t_editor.appendPlainText)
        def text_browser_signal_callback(txt:str):
            txt = "[GPT]" + txt
            txt = "<font color=\"#FF0000\">" + txt + "</font>"
            self.textBrowser.append(txt)
        
        self.text_browser_signal.connect(text_browser_signal_callback)

    # 提供给controller的页面修改回调
    def bind_controller_callback(self):

        def gpt_message_trigger_callback(msg):
            logging.info('gpt message comming=%s', msg)
            self.text_browser_signal.emit(msg)

        self.controller.bind_gpt_message_trigger(gpt_message_trigger_callback)

        def stt_message_trigger_callback(msg):
            logging.info('stt message comming=%s', msg)
            self.correct_s2t_editor_signal.emit(msg)

        self.controller.bind_stt_message_trigger(stt_message_trigger_callback)


    def release_resource(self):
        dump_config()
        self.controller.stop_thread()



