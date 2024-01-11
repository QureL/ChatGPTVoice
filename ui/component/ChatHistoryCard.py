from PySide6.QtGui import QContextMenuEvent
from PySide6.QtWidgets import QVBoxLayout, QFrame, QSizePolicy
from PySide6.QtCore import Qt, Signal
from qfluentwidgets import InfoBar, InfoBarPosition, FluentIcon, \
    RoundMenu, Action, MenuAnimationType, SubtitleLabel, \
    LineEdit, Dialog


class RenameMessageBox(Dialog):
    def __init__(self, parent=None):
        super().__init__(title="Rename Session", content="", parent=parent)
        self.newNameLineEdit = LineEdit(self)
        self.newNameLineEdit.setPlaceholderText('Input new name')
        self.newNameLineEdit.setClearButtonEnabled(True)
        for i in range(self.vBoxLayout.count()): 
            item = self.vBoxLayout.itemAt(i)
            if item.widget():
                if item.widget() == self.contentLabel:
                    self.vBoxLayout.itemAt(i).widget().setParent(None)
                    break
        self.newNameLineEdit.setFixedWidth(200)
        self.vBoxLayout.insertWidget(2, self.newNameLineEdit, 0, Qt.AlignTop | Qt.AlignmentFlag.AlignCenter)


class ChatHistoryCard(QFrame):

    def __init__(self, parent=None, title=None, selected_session_signal: Signal = None,
                 session_rename_signal: Signal = None) -> None:
        super().__init__(parent=parent)
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
        self.session_rename_signal = session_rename_signal

    def mouseDoubleClickEvent(self, event):
        self.selected_session_signal.emit(self.infoBar.title)
        super().mouseDoubleClickEvent(event)

    def contextMenuEvent(self, e: QContextMenuEvent) -> None:
        menu = RoundMenu(parent=self)
        action = Action(FluentIcon.COPY, 'Rename')
        menu.addAction(action)

        def rename_callback():
            box = RenameMessageBox(parent=None)
            if box.exec():
                if len(box.newNameLineEdit.text()) == 0:
                    return
                self.session_rename_signal.emit(self.infoBar.title, box.newNameLineEdit.text())
                self.infoBar.titleLabel.setText(box.newNameLineEdit.text())
                self.infoBar.setWindowTitle
                self.infoBar.update()
        action.triggered.connect(rename_callback)
        menu.exec(e.globalPos(), aniType=MenuAnimationType.DROP_DOWN)
