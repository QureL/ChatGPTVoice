from typing import Optional
import PySide6.QtCore
from ui.design.Ui_setting import Ui_setting_window
from PySide6.QtWidgets import QWidget
from config.config import SubtitleConfig
from config.const import *
class SettingWindow(QWidget, Ui_setting_window):

    def __init__(self, ) -> None:
        super().__init__()
        self.setupUi(self)
        self.config = SubtitleConfig()
        subtitle_sample_time = self.config.get_config(SAMPLE_TIME)
        if not subtitle_sample_time:
            self.config.set_config(SAMPLE_TIME, 10)
        
        ai_mode = self.config.get_config(SUBTITLE_AI_MODE)
        if not ai_mode:
            self.config.set_config(SUBTITLE_AI_MODE, 0)
        
        self.render_config()
        
    
    def render_config(self):
        

        self.subtitle_sample_time.setValue(int(self.config.get_config(SAMPLE_TIME)))
        self.subtitle_mode_select_combo.setCurrentIndex(int(self.config.get_config(SUBTITLE_AI_MODE)))
        self.subtitle_remote_address.setText('' if not self.config.get_config(REMOTE_ADDRESS) else self.config.get_config(REMOTE_ADDRESS))
        self.subtitle_remote_address.setEnabled(self.subtitle_mode_select_combo.currentIndex() != 0)
        def mode_select_mode_callback():
            if self.subtitle_mode_select_combo.currentIndex() == 0:
                self.subtitle_remote_address.setEnabled(False)
            else:
                self.subtitle_remote_address.setEnabled(True)

        self.subtitle_mode_select_combo.currentIndexChanged.connect(mode_select_mode_callback)

        def confirm_callback():
            self.config.set_config(SAMPLE_TIME, self.subtitle_sample_time.value())
            self.config.set_config(SUBTITLE_AI_MODE, self.subtitle_mode_select_combo.currentIndex())
            self.config.set_config(REMOTE_ADDRESS, self.subtitle_remote_address.text())
            self.close()
        
        self.subtitle_confirm.clicked.connect(confirm_callback)

        self.subtitle_setting_cancel.clicked.connect(self.close)




