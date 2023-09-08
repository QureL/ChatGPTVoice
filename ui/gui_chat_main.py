from ui.design.Ui_gpt_main_window import Ui_gpt_chat_widget
from ui.gui_gpt_session import GPTSessionSelect
from PySide6.QtWidgets import QWidget

from const import *
from gpt import gpt
import logging, sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
from config.config import GPTChatConfig
from config.const import *

from PySide6.QtCore import Signal
from controller.gpt_chat_controller import GPTChatController
from ui.custom.voice_control_button import VoiceControlButton

class GPTWidget(QWidget, Ui_gpt_chat_widget):

    text_browser_signal = Signal(str)
    correct_s2t_editor_signal = Signal(str)
    shall_correct_s2t = False

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.mode = Mode.MODE_CHAT
        
        #self.gpt_session_select_window = GPTSessionSelect(parent=self)

        self.controller = GPTChatController()
        self.config = GPTChatConfig()
        self.render_ui()

    def render_ui(self):
        self.voice_control_button = VoiceControlButton(self)
        self.verticalLayout.insertWidget(0, self.voice_control_button)


    def render_combo_boxes(self):
        self.tab1_select_input_combo.addItems(self.controller.display_audio_input_devices())
        self.tab1_select_outpt_combo.addItems(self.controller.display_audio_output_devices())

    def bind_buttons(self):
        pass

    



