from const import *
import error
from PySide6.QtCore import QThread
import logging, json
from queue import Queue
from config.config_json import load_config
from utils.pipeline import AbstractPipeline
from websocket import WebSocketApp, ABNF

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


class STT_ProcessorRemote(QThread, AbstractPipeline):

    def __init__(self,) -> None:
        QThread.__init__(self)
        self.config = load_config()
        self.stt_callback = None
    
    def set_callback(self, callback):
        self.stt_callback = callback

    def _initial_ws(self):

        def on_message(ws, message):
            result = json.loads(message)
            text_arr = [item['text'] for item in result['segments']]
            text2notify = "\n".join(text_arr)
            if self.stt_callback:
                self.stt_callback(text2notify)

        def on_error(ws, error):
            raise error

        def on_close(ws, close_status_code, close_msg):
            logging.warning("ws closed", close_status_code, close_msg)

        def on_open(ws):
            logging.debug("ws connection opened")

        self.ws = WebSocketApp(self.config.stt_remote_address,
                               on_open=on_open,
                               on_message=on_message,
                               on_error=on_error,
                               on_close=on_close)

    def run(self) -> None:
        self._initial_ws()
        self.ws.run_forever()

    def put(self, msg):
        self.ws.send(msg, ABNF.OPCODE_BINARY)

    def set_attributes(self, stt_model_name=None,
                       stt_language=None):
        logging.warn('in remote mode these set will not take effect')