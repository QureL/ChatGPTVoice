from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QWidget
from ui.design.Ui_subtitle_main_window import Ui_subtitle_main


class SubtitleMain(QWidget, Ui_subtitle_main):

    def __init__(self, ) -> None:
        super().__init__()
        self.setupUi(self)