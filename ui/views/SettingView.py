from qfluentwidgets import FluentIcon, TextEdit, PrimaryPushButton, MessageBoxBase
from qframelesswindow import FramelessWindow
from PySide6.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt


class SettingView(MessageBoxBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowIcon(FluentIcon.SETTING)
        self.setWindowTitle("Setting")
        


