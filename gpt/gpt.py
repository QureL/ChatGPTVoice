from PySide6.QtCore import QThread
import logging, os
from langchain.memory import FileChatMessageHistory
import error
from datetime import datetime
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage
from config.config_json import load_config

class GPTReuqestor:

    __instance = None
    def __init__(self, ) -> None:
        self.config = load_config()
        self.history = None
        self.__load_llm()
        self.set_system_command(self.config.gpt_sys_cmd)

    def __load_llm(self):
        self.chat_llm = ChatOpenAI(model_name=self.config.gpt_model_name,
                                   top_n=self.config.gpt_top_n,
                                   temperature=self.config.gpt_temperature,
                                   openai_api_key=self.config.openai_api_key,
                                   openai_api_base=self.config.openai_api_base)
    
    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = GPTReuqestor()
        return cls.__instance

    def set_system_command(self, cmd):
        if len(cmd) == 0: return
        self.config.gpt_sys_cmd = cmd
        self.__initial_history()
        if len(self.history.messages) == 0:
            self.history.add_message(SystemMessage(content=cmd))
        else:
            messages = self.history.messages
            messages[0] = SystemMessage(content=cmd)
            self.history.clear()
            for m in messages:
                self.history.add_message(m)

    def set_attributes(self,
                       openai_api_base=None,
                       openai_api_key=None,
                       gpt_context_cnt=None,
                       gpt_model_name=None,
                       gpt_temperature=None,
                       gpt_top_n=None):
        self.config.openai_api_base = openai_api_base or self.config.openai_api_base
        self.config.openai_api_key = openai_api_key or self.config.openai_api_key
        self.config.gpt_context_cnt = gpt_context_cnt or self.config.gpt_context_cnt
        self.config.gpt_model_name = gpt_model_name or self.config.gpt_model_name
        self.config.gpt_temperature = gpt_temperature or self.config.gpt_temperature
        self.config.gpt_top_n = gpt_top_n or self.config.gpt_top_n
        self.__load_llm()

    def __initial_history(self):
        if self.history is None:
            from gpt.loader import root_path
            self.history = FileChatMessageHistory(
                os.path.join(root_path,
                             datetime.now().strftime("%m-%d-%H_%M_%S")))

    def request(self, text):
        self.__initial_history()

        self.history.add_user_message(text)
        msgs = self.history.messages
        if self.config.gpt_context_cnt != -1 and len(
                msgs) > self.config.gpt_context_cnt:
            msgs = msgs[:1] + msgs[1 - self.config.gpt_context_cnt:]
        try:
            logging.info("requestor send message=%s", msgs)
            resp = self.chat_llm(msgs)
        except:
            raise error.BaseException()
        logging.debug("gpt resp=%s", resp.content)
        self.history.add_message(resp)
        return resp.content

    def set_session(self, session_name):
        from gpt.loader import root_path
        self.history = FileChatMessageHistory(
            os.path.join(root_path, session_name))
        messages = self.history.messages
        if len(messages) > 0 and messages[0].type == 'system':
            self.config.gpt_sys_cmd = messages[0].content



class ConcurrentGPTBridge(QThread):

    def __init__(self, gpt_requestor, speaker) -> None:
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
