import pyttsx3, nltk
from PySide6.QtCore import QThread
from queue import Queue
from utils.pipeline import AbstractPipeline
from config.config_json import load_config


class SpeakderPyTTSx3(QThread, AbstractPipeline):
    BASE_RATE = 140

    def __init__(self, ) -> None:
        self.engine = pyttsx3.init()
        self.q = Queue()
        self._running = True
        self._speaking = True
        self.config = load_config()
        super().__init__()

    def set_attributes(self, speaker_speed=None, speaker_voice=None):
        self.config.speaker_speed = speaker_speed or self.config.speaker_speed
        self.config.speaker_voice = speaker_voice or self.config.speaker_voice

        rate = int(self.BASE_RATE * self.config.speaker_speed)
        self.engine.setProperty('rate', rate)

        voices = self.engine.getProperty('voices')
        for v in voices:
            if v.name == self.config.speaker_voice:
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