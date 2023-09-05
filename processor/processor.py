from const import *
import error
from PySide6.QtCore import QThread
import logging

from websocket import WebSocketApp, ABNF
import json
from utils.pipeline import AbstractPipeline

class ResultCorrectPipeline(AbstractPipeline):
    def __init__(self, signal, output_pipe) -> None:
        self.signal = signal
        self.output_pipe = output_pipe

    def put(self, msg):
        self.signal.emit(msg)
        #self.output_pipe.put(msg)

class GPT2T2SProcessorPipeline:
    def __init__(self, signal, output_pipe) -> None:
        self.signal = signal
        self.output_pipe = output_pipe
    
    def put(self, msg):
        self.signal.emit(msg)
        self.output_pipe.put(msg)


class Speech2TextProccessor(QThread, AbstractPipeline):

    def __init__(self, ws_address,
                 output_pipe) -> None:
        self.address = ws_address
        QThread.__init__(self)
        self.output_pipe = output_pipe

    def _initial_ws(self):

        def on_message(ws, message):
            result = json.loads(message)
            text_arr = [item['text'] for item in result['segments']]
            text2notify = "\n".join(text_arr)
            self.output_pipe.put(text2notify)

        def on_error(ws, error):
            raise error

        def on_close(ws, close_status_code, close_msg):
            logging.warning("### closed ###", close_status_code, close_msg)

        def on_open(ws):
            logging.debug("Opened connection")

        self.ws = WebSocketApp(self.address,
                               on_open=on_open,
                               on_message=on_message,
                               on_error=on_error,
                               on_close=on_close)

    def run(self) -> None:
        self._initial_ws()
        self.ws.run_forever()

    def put(self, msg):
        self.ws.send(msg, ABNF.OPCODE_BINARY)


class Text2SpeechProccessor(QThread, AbstractPipeline):

    def __init__(self, ws_address, output_pipe) -> None:
        self.address = ws_address
        QThread.__init__(self)
        self.output_pipe = output_pipe

    def _initial_ws(self):

        def on_message(ws, message):
            self.output_pipe.put(message)

        def on_error(ws, error):
            raise error

        def on_close(ws, close_status_code, close_msg):
            logging.warning("### closed ###", close_status_code, close_msg)

        def on_open(ws):
            logging.debug("Opened connection")

        self.ws = WebSocketApp(self.address,
                               on_open=on_open,
                               on_message=on_message,
                               on_error=on_error,
                               on_close=on_close)

    def run(self) -> None:
        self._initial_ws()
        self.ws.run_forever()

    def put(self, msg):
        self.ws.send(msg)


class S2TLocalServer(QThread, AbstractPipeline):

    def __init__(self, model_name, language, output_pipe) -> None:
        QThread.__init__(self)
        self.model_name = model_name
        self.language = language
        from queue import Queue
        self.q = Queue()
        self.output_pipe = output_pipe


    def put(self, msg):
        self.q.put(msg)
    
    def get(self):
        return super().get()
    
    def run(self) -> None:
        import whisper
        import numpy as np

        model = whisper.load_model(self.model_name)
        logging.warning("model load success... model=%s", self.model_name)
        while True:
            msg = self.q.get()
            try:
                arr = np.frombuffer(
                    (msg), dtype=np.int16).astype(np.float32) / 32768.0

                r = json.dumps(model.transcribe(arr,))
                text_arr = [item['text'] for item in r['segments']]
                
            except:
                raise error.AITranscribeError()
            
            text2notify = "\n".join(text_arr)
            self.output_pipe.put(text2notify)
