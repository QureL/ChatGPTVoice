from typing import Optional
import PySide6.QtCore
from ui.design.Ui_main_window import Ui_main_window
from const import Mode
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout, QMainWindow

class MainWindow(QMainWindow, Ui_main_window):

    def __init__(self, mode) -> None:
        super().__init__()

        self.setupUi(self)

        if mode == Mode.MODE_SUBTITLE:
            pass

    
    def initial(self):
        self.actionsetting.triggered.connect()
