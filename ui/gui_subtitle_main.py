from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QWidget, QMessageBox
from ui.design.Ui_subtitle_main_window import Ui_subtitle_main
from config.config import SubtitleConfig
from config.const import *
from const import *
import logging, sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
class GPUDeviceInfo:
    cuda_available = False
    cuda_device_cnt = 0
    cuda_devices = []

    def get_info(self):
        import torch
        self.cuda_available = torch.cuda.is_available()
        self.cuda_device_cnt = torch.cuda.device_count()
        self.cuda_devices = [torch.cuda.get_device_name(i) for i in range(self.cuda_device_cnt)]


class SubtitleMain(QWidget, Ui_subtitle_main):

    def __init__(self, ) -> None:
        super().__init__()
        self.setupUi(self)
        from audio.audio import AudioDeviceKeepr
        self.audio_keep = AudioDeviceKeepr()

        self.render_combo_boxes()
        self.gpu_info = GPUDeviceInfo()
        self.bind_buttons()

    

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

    def environment_check(self):
        self.model_size = self.subtitle_model_select_combo.currentText()
        logging.warn('start to checking, model=%s', self.model_size)
        self.gpu_info.get_info()
        message = f"cuda可用：{self.gpu_info.cuda_available}\n"
        message += f"可用gpu数量：{self.gpu_info.cuda_device_cnt}\n"
        message += f"gpu列表：{self.gpu_info.cuda_devices}"

        QMessageBox.information(self, "环境检测", message)

    def bind_buttons(self):
        
        def start_btn_callback():
            pass

        self.start_btn.clicked.connect(start_btn_callback)
        self.check_env_btn.clicked.connect(self.environment_check)


        

