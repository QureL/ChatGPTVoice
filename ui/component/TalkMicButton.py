from qfluentwidgets import IconWidget, FluentIcon, PrimaryPushButton
import sys
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget, QHBoxLayout, QFrame
from PySide6.QtCore import Qt


class TalkMicButton(PrimaryPushButton):
    PAUSING = 1
    TALKING = 2
    def __init__(self, parent=None,):
        super().__init__(parent)
        self.setIcon(FluentIcon.MICROPHONE)
        self.setText("Talk")
        self.state = TalkMicButton.PAUSING
    
    def switch(self):
        if self.state == TalkMicButton.PAUSING:
            self.state = TalkMicButton.TALKING
            self.setIcon(FluentIcon.PAUSE)
            self.setText("Stop")
        else:
            self.state = TalkMicButton.PAUSING
            self.setIcon(FluentIcon.MICROPHONE)
            self.setText("Talk")    
    
