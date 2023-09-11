from const import *
import error
from PySide6.QtCore import QThread
import logging
from queue import Queue
from config.config_json import load_config
from websocket import WebSocketApp, ABNF
import json
from utils.pipeline import AbstractPipeline


class STT_ProcessorLocal(QThread, AbstractPipeline):

    def __init__(self) -> None:
        QThread.__init__(self)
        self.q = Queue()
        self.config = load_config()
        self.stt_callback = None


    def put(self, msg):
        logging.info("msg coming to whisper...")
        self.q.put(msg)
    
    def set_attributes(self, stt_model_name=None,
                       stt_language=None):
        changd = False
        if stt_model_name and stt_model_name != self.config.stt_model_name:
            self.config.stt_model_name = stt_model_name 
            changd = True
        if stt_language and stt_language != self.config.stt_language:
            self.config.stt_language = stt_language
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

        model = whisper.load_model(self.config.stt_model_name)
        logging.warning("model load success... model=%s", self.config.stt_model_name)
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
