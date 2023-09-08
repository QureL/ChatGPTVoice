from PySide6.QtCore import QThread
import logging, os
from langchain.memory import FileChatMessageHistory
import error
from datetime import datetime
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
import openai
from utils.dynamic_attributes import DynamicAttributes

class GPTReuqestor(DynamicAttributes):

    def __init__(self,) -> None:
        self.context_cnt = 7
        self.temperature = 1
        self.top_n = 1.5
        self._system_cmds = []
        self.gpt_model = "gpt-3.5-turbo"
        self.api_base = openai.api_base
        self.api_key = openai.api_key
        self.history = None
        self.chat_llm = ChatOpenAI(model_name=self.gpt_model, top_n=self.top_n, 
                                   temperature=1, 
                                   openai_api_key=self.api_key, 
                                   openai_api_base=self.api_base)
        

    def set_system_command(self, cmd):
        self.initial_history()
        if len(self.history.messages) == 0:
            self.history.add_message(SystemMessage(content=cmd))
        else:
            messages = self.history.messages
            messages[0] = HumanMessage(content=cmd)
            self.history.clear()
            for m in messages: self.history.add_message(m)

    def add_messages(self, messages):
        for msg in messages:
            self.history.add_message(msg)

    def set_attribute(self, **args):
        changd = False
        for key, value in args.items():
            if hasattr(self, key) and getattr(self, key) != value:
                setattr(self, key, value)
                changd = True
        if changd:
            self.chat_llm = ChatOpenAI(model_name=self.gpt_model, top_n=self.top_n, 
                                        temperature=self.temperature, 
                                        openai_api_key=self.api_key, 
                                        openai_api_base=self.api_base)

    def initial_history(self):
        if self.history is None:
            from gpt.loader import root_path
            self.history = FileChatMessageHistory(os.path.join(root_path, datetime.now().strftime("%m-%d-%H_%M_%S")))

    def request(self, text):
        self.initial_history()

        self.history.add_user_message(text)
        msgs = self.history.messages
        if self.context_cnt != -1 and len(msgs) > self.context_cnt:
            msgs = msgs[:1] + msgs[1-self.context_cnt:]
        try:
            resp = self.chat_llm(msgs)
        except:
            raise error.BaseException()
        logging.debug("gpt resp=%s", resp.content)
        self.history.add_message(resp)
        return resp.content
    
    def set_session(self, session_name):
        from gpt.loader import root_path
        self.history = FileChatMessageHistory(os.path.join(root_path, session_name))



from utils.pipeline import AbstractPipeline


class ConcurrentGPTBridge(QThread):

    def __init__(
        self,
        gpt_requestor,
        speaker
    ) -> None:
        from queue import Queue
        self.gpt_requestor = gpt_requestor
        self.q = Queue()
        self.gpt_bridge_callback = None
        self._running = True
        self.speaker = speaker
        super().__init__()

    def stop(self):
        self._running = False

    def put(self, msg):
        self.q.put(msg)

    def set_callback(self, callback):
        self.gpt_bridge_callback = callback


    def run(self) -> None:
        logging.debug("gpt bridge start...")
        while self._running:
            msg = self.q.get()
            try:
                resp = self.gpt_requestor.request(msg)
                if self.gpt_bridge_callback:
                    self.gpt_bridge_callback(resp)
                self.speaker.put(resp)
            except Exception as ex:
                logging.error("gpt requestor", ex)
                raise ex
            
