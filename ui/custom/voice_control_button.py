from PySide6.QtWidgets import QAbstractButton, QWidget
from PySide6.QtGui import QPainter, QPixmap

AUDIO_STATE_ON = 0
AUDIO_STATE_OFF = 1
class VoiceControlButton(QAbstractButton):

    def __init__(self, parent: QWidget | None = ...) -> None:
        super().__init__(parent)

        self.state = AUDIO_STATE_ON
        self.setMinimumSize(50, 50)  # 设置最小大小
        self.setMaximumSize(50, 50)  # 设置最大大小

        self.pixmap_audio_on = QPixmap("resources/speaker-on.svg")
        self.pixmap_audio_off = QPixmap('resources/speaker-on.svg')
        self.pixmap = self.pixmap_audio_on 
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(event.rect(), self.pixmap)

    
    def re_paint(self):

        if self.state == AUDIO_STATE_ON:
            self.state = AUDIO_STATE_OFF
            self.pixmap = self.pixmap_audio_off
        else:
            self.state = AUDIO_STATE_ON
            self.pixmap = self.pixmap_audio_on
        self.update()

    def resizeEvent(self, event) -> None:
        height = event.size().height()
        new_size = event.size()
        new_size.setWidth(height)
        self.resize(new_size)
    
    def sizeHint(self):
        return self.pixmap.size()


    



