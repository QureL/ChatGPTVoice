import tornado.ioloop
import tornado.web
import tornado.websocket
import json
import whisper
import logging, sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

model_name = "base"
model = whisper.load_model(model_name)
logging.warning("model load success...%s", model_name)
import numpy as np


class WebSocketHandler(tornado.websocket.WebSocketHandler):

    def open(self):
        logging.warning("open success")

    def on_close(self):
        logging.warning("closed")


    def on_message(self, message: str | bytes):
        arr = np.frombuffer(
            (message), dtype=np.int16).astype(np.float32) / 32768.0
        result = model.transcribe(arr, language='en')
        r = json.dumps(result)
        logging.warning(result)
        self.write_message(r)

application = tornado.web.Application([
    (r'/', WebSocketHandler),
])

if __name__ == '__main__':
    application.listen(3001)
    tornado.ioloop.IOLoop.instance().start()
