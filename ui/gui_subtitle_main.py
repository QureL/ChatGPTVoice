# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. 
# If a copy of the MPL was not distributed with this file, 
# You can obtain one at https://mozilla.org/MPL/2.0/.
#
# Author: qurel
# GitHub: https://github.com/QureL/horn
# Copyright reserved

from PySide6.QtWidgets import QWidget, QMessageBox
from ui.design.Ui_subtitle_main_window import Ui_subtitle_main
from config.config import SubtitleConfig
from config.const import *
from const import *
import logging, sys
from ui.gui_system_subtitle import SystemSubtitle
from PySide6.QtCore import Signal

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
    text_browser_signal = Signal(str)

    def __init__(self, ) -> None:
        super().__init__()
        self.setupUi(self)
        from audio.audio import AudioDeviceKeepr
        self.audio_keep = AudioDeviceKeepr()

        self.render_combo_boxes()
        self.gpu_info = GPUDeviceInfo()
        self.bind_buttons()
        self.system_subtitle = SystemSubtitle()
        self.initial_processor_record()
        self.bind_signal()

    

    def render_combo_boxes(self):
        devices_current = self.audio_keep.display_devices(input=True)
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
            self.system_subtitle.show()
            self.start_proccessor_recorder()

        self.start_btn.clicked.connect(start_btn_callback)
        self.check_env_btn.clicked.connect(self.environment_check)

    def release_resource(self):
        self.system_subtitle.close()
        self.proccessor.terminate()
        self.recorder.terminate()

    
    def bind_signal(self):
        self.text_browser_signal.connect(self.system_subtitle.update)

    def initial_processor_record(self):
        from processor.processor import S2TLocalServer
        from config.config import SubtitleConfig
        from audio.audio import AudioRecorder
        model_name = self.subtitle_model_select_combo.currentText()
        language = self.subtitle_language_select_combo.currentText()
        self.proccessor = S2TLocalServer(model_name=model_name,
                                         language=language,
                                         signal=self.text_browser_signal)
        self.config = SubtitleConfig()
        secs = int(self.config.get_config(SAMPLE_TIME))
        
        self.recorder = AudioRecorder(
            keeper=self.audio_keep,
            output_pipe=self.proccessor,
            is_chat=False,
            secs=secs
        )
    
    def start_proccessor_recorder(self):
        self.recorder.select_device(self.subtitle_input_select_combo.currentText())
        self.recorder.start_timer()
        self.proccessor.start()
        self.recorder.start()
        





        

