from const import *
import error
from PySide6.QtCore import QThread
import logging

from websocket import WebSocketApp, ABNF
import json
from utils.pipeline import AbstractPipeline
from utils.dynamic_attributes import DynamicAttributes


class STT_ProcessorLocal(QThread, AbstractPipeline, DynamicAttributes):

    def __init__(self, stt_model, stt_language) -> None:
        QThread.__init__(self)
        self.stt_model = stt_model
        self.stt_language = stt_language
        from queue import Queue
        self.q = Queue()
        self.stt_callback = None


    def put(self, msg):
        logging.info("msg coming to whisper...")
        self.q.put(msg)
    
    def set_attribute(self, **args):
        changd = False
        for key, value in args.items():
            if hasattr(self, key) and getattr(self, key) != value:
                setattr(self, key, value)
                changd = True
        if changd:
            if self.isRunning():
                self.terminate()
                self.start()
    
    def set_callback(self, callback):
        self.stt_callback = callback
    
    def run(self) -> None:
        import whisper
        import numpy as np

        model = whisper.load_model(self.stt_model)
        logging.warning("model load success... model=%s", self.stt_model)
        while True:
            msg = self.q.get()
            try:
                arr = np.frombuffer(
                    (msg), dtype=np.int16).astype(np.float32) / 32768.0
                result = model.transcribe(arr,)
                logging.debug("result=%s", result)
                text_arr = [item['text'] for item in result['segments']]
                
            except Exception as e:
                logging.error(e)
                raise error.AITranscribeError()
            
            text2notify = "\n".join(text_arr)
            if self.stt_callback:
                self.stt_callback(text2notify)
