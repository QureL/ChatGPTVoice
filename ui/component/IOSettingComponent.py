from typing import Optional
from qfluentwidgets import ScrollArea, IconWidget, FluentIcon, ComboBox
from qframelesswindow import FramelessWindow
import sys
from PySide6.QtWidgets import QApplication, QVBoxLayout, QLabel, QFrame, QHBoxLayout, QSizePolicy
from PySide6.QtCore import Qt

class IOSettingComponent(QFrame):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setFixedWidth(500)
        self.labelsLayout = QVBoxLayout()
        self.commboLayout = QVBoxLayout()
        self.layout = QHBoxLayout(self)
        self.layout.addLayout(self.labelsLayout)
        self.layout.addLayout(self.commboLayout)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        

        self.labelSelectInputDevice = QLabel("Select Input Device", self)
        sizePolicy.setHeightForWidth(self.labelSelectInputDevice.sizePolicy().hasHeightForWidth())
        self.labelSelectInputDevice.setSizePolicy(sizePolicy)
        self.labelSelectGPTOutputDevice = QLabel("Select GPT Output", self)
        sizePolicy.setHeightForWidth(self.labelSelectGPTOutputDevice.sizePolicy().hasHeightForWidth())
        self.labelSelectGPTOutputDevice.setSizePolicy(sizePolicy)

        self.commboxSelectInputDevice = ComboBox(self)
        self.commboxSelectGPTOutputDevice = ComboBox(self)

        self.labelsLayout.addWidget(self.labelSelectInputDevice)
        self.labelsLayout.addWidget(self.labelSelectGPTOutputDevice)
        self.commboLayout.addWidget(self.commboxSelectInputDevice)
        self.commboLayout.addWidget(self.commboxSelectGPTOutputDevice)

if __name__  == '__main__':
    app = QApplication(sys.argv)
    w = IOSettingComponent()
    w.show()
    app.exec()