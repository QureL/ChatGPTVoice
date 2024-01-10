from qfluentwidgets import ScrollArea, IconWidget, FluentIcon
import sys
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QHBoxLayout, QFrame, QSizePolicy
from ui.component.ChatItem import ChatItem
from PySide6.QtCore import QEvent, QObject, Qt
class ChatArea(ScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.horizontalScrollBar().setValue(0)
        self.setFixedHeight(450)
        self.setMinimumWidth(500)
        self.contentWidget = QWidget()

        self.layout = QVBoxLayout(self.contentWidget)
        self.layout.setContentsMargins(10, 10, 10, 10)
        self.layout.setSpacing(2)
        self.layout.setAlignment(Qt.AlignTop)
        self.setWidget(self.contentWidget)
        self.setWidgetResizable(True)
        self.setStyleSheet("background-color: #F0F8FF;border: none;") 

    def add_human_message(self, content):
        frame = QFrame(self.contentWidget)
        card = ChatItem(ChatItem.HUMAN, content, frame)
        hLayout = QHBoxLayout(frame)
        hLayout.addWidget(card)
        self.layout.addWidget(frame, 0, Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)

    def add_bot_message(self, content):
        frame = QFrame(self.contentWidget)
        card = ChatItem(ChatItem.BOT, content, frame)
        hLayout = QHBoxLayout(frame)
        hLayout.addWidget(card)
        self.layout.addWidget(frame, 0, Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
    
    def clear_message(self):
        for i in reversed(range(self.layout.count())): 
            self.layout.itemAt(i).widget().setParent(None)

    # 自动滚动到最底部
    def eventFilter(self, arg__1: QObject, arg__2: QEvent) -> bool:
        if isinstance(arg__1, QWidget) and arg__2.type() == QEvent.Resize:
            self.verticalScrollBar().setMaximum(arg__1.height() + self.verticalScrollBar().maximum())
            self.verticalScrollBar().setValue(self.verticalScrollBar().maximum()+ arg__1.height())
            return False
        return super().eventFilter(arg__1, arg__2)
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ChatArea()
    for i in range(29):
        if i % 3 == 0:
            w.add_bot_message(f"testfdasfsfsdfadsrewewr fdsfa afsarewfdss asfarevtest{i}")
        else:
            w.add_human_message(f" t{i}")
    w.show()
    app.exec()