from qfluentwidgets import ScrollArea, IconWidget, FluentIcon
from qframelesswindow import FramelessWindow
import sys
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget
from PySide6.QtCore import Qt

class GPTChatMain(FramelessWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

