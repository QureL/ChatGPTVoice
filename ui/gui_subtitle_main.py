from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QWidget
from ui.design.Ui_subtitle_main_window import Ui_subtitle_main
from config.config import SubtitleConfig
from config.const import *
from const import *
class SubtitleMain(QWidget, Ui_subtitle_main):

    def __init__(self, ) -> None:
        super().__init__()
        self.setupUi(self)
        from audio.audio import AudioDeviceKeepr
        self.audio_keep = AudioDeviceKeepr()

        self.render_combo_boxes()

    

    def render_combo_boxes(self):
        devices_current = self.audio_keep.display_devices()
        self.subtitle_input_select_combo.addItems(devices_current)
        config = SubtitleConfig()
        device_before =  config.get_config(SUBTITLE_INPUT_DEVICE)
        if device_before in devices_current:
            self.subtitle_input_select_combo.setCurrentText(device_before)

        models = [e.value for e in ModelSize]
        self.subtitle_model_select_combo.addItems(models)
        model_before = config.get_config(S2T_MODEL_SIZE)
        if model_before in models:
            self.subtitle_model_select_combo.setCurrentText(model_before)

        language = config.get_config(S2T_LANGUAGE)
        languages = [e.value for e in Language]
        self.subtitle_language_select_combo.addItems(languages)
        if language in languages:
            self.subtitle_language_select_combo.setCurrentText(language)



        

