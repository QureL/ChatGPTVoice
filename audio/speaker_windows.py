import pyttsx3, nltk
from PySide6.QtCore import QThread
from queue import Queue

class SpeakderPyTTSx3(QThread):
    BASE_RATE = 140

    def __init__(self, speed=1) -> None:
        self.engine = pyttsx3.init()
        self.set_speed(speed)
        self.q = Queue()
        self._running = True
        self._speaking = True
        super().__init__()

    def set_speed(self, speed):
        self.rate = self.BASE_RATE* speed
        self.engine.setProperty('rate', self.rate)

    def select_voice(self, device_name):
        voices = self.engine.getProperty('voices')
        for v in voices:
            if v.name == device_name:
                self.engine.setProperty('voice', v.id)

    def show_voices(self):
        voices = self.engine.getProperty('voices')
        return [v.name for v in voices]

    def run(self) -> None:
        while self._running:
            txt = self.q.get()
            txt = txt.replace('\n', ' ')
            sentences = nltk.sent_tokenize(txt)
            self._last_speech = sentences
            i = 0
            while self._speaking and i < len(sentences):
                self.engine.say(sentences[i])
                i += 1
                self.engine.runAndWait()
    
    def put(self, audio):
        self.q.put(audio)

    def stop(self):
        self._running = False

    def speak_again(self):
        pass

    def pause(self):
        self._speaking = not self._speaking