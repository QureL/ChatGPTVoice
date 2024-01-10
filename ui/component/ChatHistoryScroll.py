from qfluentwidgets import ScrollArea
from gpt.loader import display_history_sessions
import sys
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget
from ui.component.ChatHistoryCard import ChatHistoryCard
from PySide6.QtCore import Qt, Signal
class ChatHistoryScroll(ScrollArea):
    selected_session_signal = Signal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.horizontalScrollBar().setValue(0)
        self.setFixedWidth(200)
        self.contentWidget = QWidget()
        self.layout = QVBoxLayout(self.contentWidget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(2)
        self.setWidget(self.contentWidget)
        self.setWidgetResizable(True)
        self.setStyleSheet("background-color: #FFFFCC;border: none;")
        self.layout.setAlignment(Qt.AlignTop)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
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
