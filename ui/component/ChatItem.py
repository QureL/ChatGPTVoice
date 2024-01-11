import sys
from typing import Union
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QVBoxLayout, QFrame, QLabel, QSizePolicy
from PySide6.QtCore import Qt
from qfluentwidgets import InfoBar, InfoBarIcon, InfoBarPosition, FluentIcon
from qfluentwidgets.common.icon import FluentIconBase
class ChatItem(InfoBar):
    BOT = 1
    HUMAN = 2
    def __init__(self, type, content, parent=None):
        if type == ChatItem.BOT:
            icon = FluentIcon.ROBOT
            title = "Bot"
            positon = InfoBarPosition.NONE
            color = "#FFD700"
        else:
            icon = FluentIcon.PEOPLE
            title = "Human"
            positon = InfoBarPosition.NONE
            color = "#6495ED"
        super().__init__(icon, title, content, orient=Qt.Vertical, 
                         isClosable=False, duration=-1, 
                         position=positon, parent=parent)
        self.setCustomBackgroundColor(color, color)