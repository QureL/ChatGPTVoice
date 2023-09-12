from typing import Optional
import PySide6.QtCore
from ui.design.Ui_main_window import Ui_main_window
from const import Mode
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout, QMainWindow

class MainWindow(QMainWindow, Ui_main_window):

    def __init__(self, mode) -> None:
        super().__init__()

        self.setupUi(self)

        #self.initial()
        if mode == Mode.MODE_SUBTITLE:
            from ui.gui_subtitle_main import SubtitleMain
            self.subtitle_main = SubtitleMain()
            self.setCentralWidget(self.subtitle_main)
        else:
            from ui.gui_chat_main import GPTWidget
            self.gpt_chat_main = GPTWidget()
            self.setCentralWidget(self.gpt_chat_main)
            

    
    #def initial(self):
    #    from ui.setting_window import SettingWindow
    #    self.setting_window = SettingWindow()
    #    self.actionsetting.triggered.connect(self.setting_window.show)

    def closeEvent(self, event) -> None:
        #self.subtitle_main.release_resource()
        self.gpt_chat_main.release_resource()
