from typing import Optional
import PySide6.QtCore
from ui.design.Ui_setting import Ui_setting_window
from PySide6.QtWidgets import QWidget


class SettingWindow(QWidget, Ui_setting_window):

    def __init__(self, ) -> None:
        super().__init__()
        self.setupUi(self)