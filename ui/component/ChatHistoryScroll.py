from qfluentwidgets import ScrollArea, IconWidget, FluentIcon
import sys
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget
from ChatHistoryCard import ChatHistoryCard
from PySide6.QtCore import Qt
class ChatHistoryScroll(ScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.horizontalScrollBar().setValue(0)
        self.setFixedSize(200, 700)
        self.contentWidget = QWidget()
        self.layout = QVBoxLayout(self.contentWidget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(2)
        self.setWidget(self.contentWidget)
        self.setWidgetResizable(True)
        self.setStyleSheet("background-color: #6699CC;")

    def add_history(self, title):
        card = ChatHistoryCard(title)
        self.layout.addWidget(card, 0, Qt.AlignTop)

    def delete_history(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ChatHistoryScroll()
    for i in range(20):
        w.add_history(f"testtest{i}")
    w.show()
    app.exec()
