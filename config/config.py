import os, sys
from PySide6.QtCore import QSettings

import const

config_base_path = os.path.join(os.path.expanduser("~"), 'AppData', 'Local',
                                f'{const.APP_NAME}.ini')

class SubtitleConfig:

    group = "SUBTITLE/"

    def __init__(self) -> None:
        self.setting = QSettings(config_base_path, QSettings.IniFormat)
    
    def get_config(self, key:str):
        return self.setting.value(self.group + key)
    
    def set_config(self, key:str, value):
        self.setting.setValue(self.group + key, value)

class GPTChatConfig:
    group = "GPT/"

    def __init__(self) -> None:
        self.setting = QSettings(config_base_path, QSettings.IniFormat)
    
    def get_config(self, key:str):
        return self.setting.value(self.group + key)
    
    def set_config(self, key:str, value):
        self.setting.setValue(self.group + key, value)
