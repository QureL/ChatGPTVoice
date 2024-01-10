from qfluentwidgets import ScrollArea, IconWidget, FluentIcon
import sys
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QHBoxLayout, QFrame, QSizePolicy
from ChatItem import ChatItem
from PySide6.QtCore import Qt
class ChatArea(ScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.horizontalScrollBar().setValue(0)
        self.setFixedSize(500, 500)
        self.contentWidget = QWidget()

        self.layout = QVBoxLayout(self.contentWidget)
        self.layout.setContentsMargins(10, 10, 10, 10)
        self.layout.setSpacing(2)
        self.setWidget(self.contentWidget)
        self.setWidgetResizable(True)
        self.setStyleSheet("background-color: #F0F8FF;") 

    def add_human_message(self, content):
        card = ChatItem(ChatItem.HUMAN, content)
        frame = QFrame(self.contentWidget)
        hLayout = QHBoxLayout(frame)
        hLayout.addWidget(card)
        self.layout.addWidget(frame, 0, Qt.AlignmentFlag.AlignRight)

    def add_bot_message(self, content):
        card = ChatItem(ChatItem.BOT, content)
        frame = QFrame(self.contentWidget)
        hLayout = QHBoxLayout(frame)
        hLayout.addWidget(card)
        self.layout.addWidget(frame, 0, Qt.AlignmentFlag.AlignLeft)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ChatArea()
    for i in range(20):
        if i % 3 == 0:
            w.add_bot_message(f"testfdasfsfsdfadsrewewr fdsfa afsarewfdss asfarevtest{i}")
        else:
            w.add_human_message(f" t{i}")
    w.show()
    app.exec()