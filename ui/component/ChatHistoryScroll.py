from qfluentwidgets import ScrollArea
from gpt.loader import display_history_sessions, rename_session
import sys
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel
from ui.component.ChatHistoryCard import ChatHistoryCard
from PySide6.QtCore import Qt, Signal
class ChatHistoryScroll(ScrollArea):
    selected_session_signal = Signal(str)
    session_rename_signal = Signal(str, str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.horizontalScrollBar().setValue(0)
        self.setFixedWidth(250)
        self.contentWidget = QWidget()
        self.layout = QVBoxLayout(self.contentWidget)
        self.layout.setContentsMargins(20, 30, 10, 10)
        self.layout.setSpacing(2)
        title = QLabel("GPT Voice Talk", self)
        title.setStyleSheet("font: 22px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';color: black;font-weight: 600;")
        self.setWidget(self.contentWidget)
        self.setWidgetResizable(True)
        self.setStyleSheet("background-color: #F0F8FF;border: none;")
        self.layout.setAlignment(Qt.AlignTop)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.layout.addWidget(title, 0, Qt.AlignTop)
        tip = QLabel("History sessions.\nDouble click to switch.\nRight click to edit session.", self)
        self.layout.addWidget(tip, 0, Qt.AlignTop)
        self.layout.addSpacing(20)
        self._render_history_session()
        self.bind_signal()

    def add_history(self, title):
        card = ChatHistoryCard(self, title, self.selected_session_signal, self.session_rename_signal)
        self.layout.addWidget(card, 0, Qt.AlignTop)

    def delete_history(self):
        pass

    def _render_history_session(self):
        sessions = display_history_sessions()
        for session in sessions:
            self.add_history(session)  
    
    def bind_signal(self):
        def rename_session_callback(old_name, new_name):
            rename_session(old_name, new_name)
        self.session_rename_signal.connect(rename_session_callback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = ChatHistoryScroll()

    w.show()
    app.exec()
