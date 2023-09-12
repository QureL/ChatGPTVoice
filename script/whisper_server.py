import tornado.ioloop
import tornado.web
import tornado.websocket
import json
import whisper
import logging, sys, argparse
import numpy as np

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


parser = argparse.ArgumentParser(description='Start a remote whisper server.')
parser.add_argument('--model', dest='model',
                    help="whisper model, tiny base or large-v2", default='base')
parser.add_argument('--language', dest='language',
                    help='en zh or jp...',
                    default="")
args = parser.parse_args()

# loading model
model_name = args.model
model = whisper.load_model(model_name)
logging.warning("model load success...%s", model_name)

class WebSocketHandler(tornado.websocket.WebSocketHandler):

    def open(self):
        logging.warning("ws open success")

    def on_close(self):
        logging.warning("ws closed")

    def on_message(self, message: str | bytes):
        arr = np.frombuffer(
            (message), dtype=np.int16).astype(np.float32) / 32768.0
        if len(args.language) > 0: 
            result = model.transcribe(arr, language=args.language)
        else:
            result = model.transcribe(arr,)
        r = json.dumps(result)
        logging.warning(result)
        self.write_message(r)

application = tornado.web.Application([
    (r'/', WebSocketHandler),
])

if __name__ == '__main__':
    application.listen(3001)
    tornado.ioloop.IOLoop.instance().start()
