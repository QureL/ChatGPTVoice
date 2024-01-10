import sys
from PySide6.QtWidgets import QApplication, QVBoxLayout, QFrame, QLabel, QSizePolicy
from PySide6.QtCore import Qt
from qfluentwidgets import InfoBar, InfoBarIcon, InfoBarPosition, FluentIcon
class ChatHistoryCard(QFrame):

    def __init__(self, title=None) -> None:
        super().__init__()
        self.infoBar = InfoBar(
            icon=FluentIcon.CHAT,
            title=title,
            content="",
            orient=Qt.Horizontal,
            isClosable=False,
            duration=-1,
            position=InfoBarPosition.NONE,
            parent=self
        )
        self.infoBar.setFixedSize(180, 50)
        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.setContentsMargins(1, 1, 1, 1)
        self.vBoxLayout.setAlignment(Qt.AlignCenter)
        self.vBoxLayout.addWidget(self.infoBar)



