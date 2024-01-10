import sys
from PySide6.QtWidgets import QVBoxLayout, QFrame, QSizePolicy
from PySide6.QtCore import Qt, Signal
from qfluentwidgets import InfoBar, InfoBarPosition, FluentIcon


class ChatHistoryCard(QFrame):

    def __init__(self, title=None, selected_session_signal: Signal = None) -> None:
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
        # self.infoBar.setFixedSize(180, 50)
        self.infoBar.setCustomBackgroundColor("#CCFFCC", "#CCFFCC")
        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.setSpacing(0)
        self.vBoxLayout.setContentsMargins(1, 1, 1, 1)
        self.vBoxLayout.setAlignment(Qt.AlignCenter)
        self.vBoxLayout.addWidget(self.infoBar)
        self.setFixedHeight(50)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.selected_session_signal = selected_session_signal

    def mouseDoubleClickEvent(self, event):
        self.selected_session_signal.emit(self.infoBar.title)
        super().mouseDoubleClickEvent(event)
