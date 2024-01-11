from qfluentwidgets import ScrollArea
from gpt.loader import display_history_sessions
import sys
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel
from ui.component.ChatHistoryCard import ChatHistoryCard
from PySide6.QtCore import Qt, Signal
class ChatHistoryScroll(ScrollArea):
    selected_session_signal = Signal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.horizontalScrollBar().setValue(0)
        self.setFixedWidth(250)
        self.contentWidget = QWidget()
        self.layout = QVBoxLayout(self.contentWidget)
        self.layout.setContentsMargins(20, 30, 10, 10)
        self.layout.setSpacing(2)
        title = QLabel("GPT Voice Talk", self)
        title.setStyleSheet("font: 22px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';color: black;font-weight: 500;")
        self.setWidget(self.contentWidget)
        self.setWidgetResizable(True)
        self.setStyleSheet("background-color: #F0F8FF;border: none;")
        self.layout.setAlignment(Qt.AlignTop)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.layout.addWidget(title, 0, Qt.AlignTop)
        tip = QLabel("History session.\nDouble click to switch.", self)
        self.layout.addWidget(tip, 0, Qt.AlignTop)
        self.layout.addSpacing(20)
        self._render_history_session()

    def add_history(self, title):
        card = ChatHistoryCard(title, self.selected_session_signal)
        self.layout.addWidget(card, 0, Qt.AlignTop)

    def delete_history(self):
        pass

    def _render_history_session(self):
        sessions = display_history_sessions()
        for session in sessions:
            self.add_history(session)  

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ChatHistoryScroll()

    w.show()
    app.exec()
