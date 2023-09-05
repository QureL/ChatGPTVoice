from PySide6.QtCore import QThread
import random
import logging
from langchain.memory import FileChatMessageHistory
import os
from datetime import datetime
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

SUMARRY_HEAD = '[SUMMARRY]:'


class GPTReuqestor:

    def __init__(self, token: str, url: str, 
                 model="gpt-3.5-turbo",
                 context_cnt=7) -> None:
        self.context_cnt = context_cnt
        self.temperature = 1
        self.top_n = 1.5
        self._system_cmds = []
        self.history = None
        self.chat_llm = ChatOpenAI(model_name=model, top_n=self.top_n, temperature=1, openai_api_key=token, openai_api_base=url)

    def set_system_command(self, commands):
        self._system_cmds = commands

    def add_messages(self, messages):
        for msg in messages:
            self.history.add_message(msg)


    def preload(text):
        if text is None:
            pass

    def request(self, text):
        if self.history is None:
            self.history = FileChatMessageHistory(os.path.join(os.getcwd(), 'data', 'messages', datetime.now().strftime("%m-%d-%H_%M_%S")))
            for cmd in self._system_cmds:
                role = list(cmd.keys())[0]
                if role == 'system':
                    self.history.add_message(SystemMessage(content=list(cmd.values())[0]))

        self.history.add_user_message(text)
        msgs = self.history.messages
        if self.context_cnt != -1 and len(msgs) > self.context_cnt:
            msgs = msgs[:1] + msgs[1-self.context_cnt:]
        logging.debug("msg send=%s", msgs)
        resp = self.chat_llm(msgs)
        logging.debug("gpt resp=%s", resp.content)
        self.history.add_message(resp)
        return resp.content
    
    def set_session(self, session_name):
        self.history = FileChatMessageHistory(os.path.join(os.getcwd(), 'data', 'messages', session_name))



from utils.pipeline import AbstractPipeline


class ConcurrentGPTBridge(QThread):

    def __init__(
        self,
        gpt_requestor,
        output_pipe: AbstractPipeline,
    ) -> None:
        from queue import Queue
        self.gpt_requestor = gpt_requestor
        self.q = Queue()
        self.output_pipe = output_pipe
        self._running = True
        super().__init__()

    def stop(self):
        self._running = False

    def put(self, msg):
        self.q.put(msg)


    def run(self) -> None:
        logging.debug("gpt bridge start...")
        while self._running:
            msg = self.q.get()
            try:
                resp = self.gpt_requestor.request(msg)
                self.output_pipe.put(resp)
            except Exception as ex:
                logging.error("gpt requestor", ex)
            
