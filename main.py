# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0.
# If a copy of the MPL was not distributed with this file,
# You can obtain one at https://mozilla.org/MPL/2.0/.
#
# Author: qurel
# GitHub: https://github.com/QureL/horn
# Copyright reserved

from hook import UncaughtHook
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QFrame
import sys
import os
from PySide6.QtCore import QThread, Signal, Qt
from qframelesswindow import FramelessWindow, StandardTitleBar
from qfluentwidgets import ComboBox, StrongBodyLabel, PrimaryPushButton, CheckBox, IndeterminateProgressRing
import argparse
from config.config_json import load_config
sys.path.append(os.getcwd())


class BackgroudImport(QThread):
    signal = Signal(str)

    def __init__(self) -> None:
        super().__init__()

    def run(self) -> None:
        import pyttsx3
        import nltk
        nltk.download('punkt')
        import pyaudio
        config = load_config()
        if config.stt_mode == 'local':
            import whisper
        import langchain
        self.signal.emit("")


class LoadingLabel(QLabel):

    def sizeHint(self):
        return self.movie().scaledSize()


class Entrance(FramelessWindow):

    def __init__(self,) -> None:
        super().__init__()
        self.setTitleBar(StandardTitleBar(self))
        self.setWindowTitle("GPT-Talk-Local")
        self.resize(300, 400)
        desktop = QApplication.primaryScreen().size()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)

        self.vBoxLayout = QVBoxLayout(self)
        self.frame = QFrame(self)

        self.frameLayout = QVBoxLayout(self.frame) 
        self.frameLayout.setSpacing(5)
        self.frameLayout.setContentsMargins(0, 0, 0, 0)

        self.comboBox = ComboBox(self.frame)
        self.titleLabel = StrongBodyLabel("Please Select Function", self.frame)
        self.confirmBtn = PrimaryPushButton("OK")
        self.shoudPreLoadCheckBox = CheckBox("Pre load dependency")
        self.loadRing = IndeterminateProgressRing(self.frame, False)
        
        self.frameLayout.addWidget(self.titleLabel)
        self.frameLayout.addWidget(self.comboBox)
        self.frameLayout.addWidget(self.shoudPreLoadCheckBox)
        self.frameLayout.addWidget(self.confirmBtn)
        self.frameLayout.addWidget(self.loadRing, 0, Qt.AlignCenter)
        self.render()
        self.hook = UncaughtHook()

    def render(self,):
        self.comboBox.addItems(["gpt voice talk locally"])
        self.vBoxLayout.addWidget(self.frame, 0, Qt.AlignCenter)
        self.confirmBtn.clicked.connect(self.confirmBtnCallBack)

    def confirmBtnCallBack(self):
        index = self.comboBox.currentIndex()
        from const import Mode
        if index == 0:
            self.mode = Mode.MODE_CHAT
        else:
            self.mode = Mode.MODE_SUBTITLE
        
        if self.shoudPreLoadCheckBox.isChecked():
            self.loadRing.start()
            self.thread = BackgroudImport()
            self.thread.signal.connect(self.import_success_callback)
            self.thread.start()
        else:
            self.import_success_callback()

    def import_success_callback(self):
        from ui.views.GPTChatMain import GPTChatMain
        self.child = GPTChatMain()
        self.child.show()
        self.close()


parser = argparse.ArgumentParser(description='Input values for horn')
parser.add_argument('--whisper_mode', dest='whisper_mode',
                    help="whisper mode, local/remote", default='local')
parser.add_argument('--whisper_address', dest='whisper_address',
                    help='if mode=remote, then set you whisper remote websocket address here',
                    default="")
parser.add_argument('--proxy', dest="proxy",
                    help="http proxy address, such as http://127.0.0.1:10809")
args = parser.parse_args()
config = load_config()
if args.whisper_mode != 'local':
    config.stt_mode = 'remote'
    config.stt_remote_address = args.whisper_address
else:
    config.stt_mode = 'local'

if args.proxy is not None:
    os.environ['HTTP_PROXY'] = os.environ['HTTPS_PROXY'] = args.proxy

app = QApplication([])


window = Entrance()
window.show()
app.exec()
