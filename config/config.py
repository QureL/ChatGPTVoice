import os, sys
from PySide6.QtCore import QSettings

import const

config_base_path = os.path.join(os.path.expanduser("~"), 'AppData', 'Local', 
                                f'{const.APP_NAME}',
                                f'{const.APP_NAME}.ini')

class ConfigBase:
    group = ""

    def __init__(self) -> None:
        self.setting = QSettings(config_base_path, QSettings.IniFormat)
    
    def get_config(self, key:str):
        return self.setting.value(self.group + key)
    
    def set_config(self, key:str, value):
        if value == None: return
        self.setting.setValue(self.group + key, value)

class SubtitleConfig(ConfigBase):

    def __init__(self) -> None:
        super().__init__()
        self.group = "SUBTITLE/"

class GPTChatConfig(ConfigBase):

    def __init__(self) -> None:
        super().__init__()
        self.group = "GPT/"
