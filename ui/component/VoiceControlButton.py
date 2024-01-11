from qfluentwidgets import IconWidget, FluentIcon, PrimaryToolButton



class VoiceControlButton(PrimaryToolButton):
    
    def __init__(self, parent=None,):
        super().__init__(parent)
        self.setIcon(FluentIcon.MUTE)
        self.have_voice = True
    
    def switch(self):
        if self.have_voice:
            self.setIcon(FluentIcon.VOLUME)
            self.have_voice = False
        else:
            self.setIcon(FluentIcon.MUTE)
            self.have_voice = True

    
