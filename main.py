import sys, os
from PySide6.QtCore import QThread, Signal
import argparse
from config.config_json import load_config
sys.path.append(os.getcwd())

from ui.design.Ui_select_function import Ui_Form
from PySide6.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout
from PySide6.QtGui import QMovie
from hook import UncaughtHook

class BackgroudImport(QThread):
    signal = Signal(str)
    def __init__(self) -> None:
        super().__init__()

    def run(self) -> None:
        import pyttsx3, nltk
        import pyaudio
        config = load_config()
        if config.stt_mode == 'local': import whisper
        import langchain
        self.signal.emit("")

class LoadingLabel(QLabel):
    
    def sizeHint(self):
        return self.movie().scaledSize()

class Entrance(QWidget, Ui_Form):

    def __init__(self,) -> None:
        super().__init__()
        self.setupUi(self)

        self.hook = UncaughtHook()

        self.pushButton.clicked.connect(self.confirm_btn_callback)
    
    def confirm_btn_callback(self):
        index = self.select_funcion_combo.currentIndex()
        movie = QMovie('./resources/loading.gif')
        label = LoadingLabel(self)
        label.setMovie(movie)
        label.adjustSize()
        label2 = QLabel("loading...", self)
        self.horizontalLayout_loading = QHBoxLayout()
        self.horizontalLayout_loading.addWidget(label)
        self.horizontalLayout_loading.addWidget(label2)
        from const import Mode
        if index == 0:
            self.mode = Mode.MODE_CHAT
        else:
            self.mode = Mode.MODE_SUBTITLE
        self.thread = BackgroudImport()
        self.thread.signal.connect(self.import_success_callback)
        self.thread.start()
        self.verticalLayout.addLayout(self.horizontalLayout_loading)
        movie.start()
            
            

    def import_success_callback(self):
        from ui.main_window import MainWindow
        self.child = MainWindow(self.mode)
        self.child.show()
        self.close()


parser = argparse.ArgumentParser(description='Input values for horn')
parser.add_argument('--whisper_mode', dest='whisper_mode',
                    help="whisper mode, local/remote", default='local')
parser.add_argument('--whisper_address', dest='whisper_address',
                    help='if mode=remote, then set you whisper remote websocket address here',
                    default="")
args = parser.parse_args()
config = load_config()
if args.whisper_mode != 'local':
    config.stt_mode = 'remote'
    config.stt_remote_address = args.whisper_address

app = QApplication([])


from PySide6.QtCore import QFile
styleFile = QFile( "./css/MacOS.css" )
styleFile.open(QFile.ReadOnly)
app.setStyleSheet(styleFile.readAll().toStdString())


window = Entrance()
window.show()
app.exec()
