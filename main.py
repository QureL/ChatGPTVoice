import sys, os
from typing import Optional

import PySide6.QtCore

sys.path.append(os.getcwd())

from ui.design.Ui_select_function import Ui_Form
from PySide6.QtWidgets import QWidget, QApplication
from hook import UncaughtHook


class Entrance(QWidget, Ui_Form):

    def __init__(self,) -> None:
        super().__init__()
        self.setupUi(self)

        self.hook = UncaughtHook()

        self.pushButton.clicked.connect(self.confirm_btn_callback)
    
    def confirm_btn_callback(self):
        index = self.select_funcion_combo.currentIndex()
        if index == 0:
            pass
        else:
            import pyttsx3, nltk
            engine = pyttsx3.init()
            print(123)





app = QApplication([])
from qt_material import apply_stylesheet
#apply_stylesheet(app, theme="dark_blue.xml")
window = Entrance()
window.show()
app.exec()
