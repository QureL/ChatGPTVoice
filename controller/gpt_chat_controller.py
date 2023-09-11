from controller.controller import Controller
from audio.audio import AudioDeviceKeepr, AudioRecorder
from audio.speaker_windows import SpeakderPyTTSx3
from config.config import GPTChatConfig
from processor.processor import STT_ProcessorLocal
from gpt.gpt import GPTReuqestor, ConcurrentGPTBridge
import enum
import logging
from config.const import *
class ControllerState(enum.Enum):
    CONTROLLER_STOPPING = 0
    CONTROLLER_RUNNING = 1


class GPTChatController():

    __instance = None

    def __init__(self,) -> None:
        self.audio_device_keeper = AudioDeviceKeepr()
        self.speaker = SpeakderPyTTSx3()
        self.stt_processor = STT_ProcessorLocal()
        self.gpt_requestor = GPTReuqestor.get_instance()
        self.gpt_bridge = ConcurrentGPTBridge(self.gpt_requestor, speaker=self.speaker)
        self.recorder = AudioRecorder(self.audio_device_keeper, output_pipe=self.stt_processor, is_chat=True, secs=10)
        self.state = ControllerState.CONTROLLER_STOPPING

        
    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = GPTChatController()
        return cls.__instance


    def display_audio_input_devices(self):
        return self.audio_device_keeper.display_devices(input=True)

    def display_audio_voices(self):
        return self.speaker.show_voices()

    def start_thread(self):
        self.speaker.start()
        self.stt_processor.start()
        self.gpt_bridge.start()
        self.recorder.start()
        self.state = ControllerState.CONTROLLER_RUNNING

    def stop_thread(self):
        self.speaker.terminate()
        self.stt_processor.terminate()
        self.gpt_bridge.terminate()
        self.recorder.terminate()
        self.state = ControllerState.CONTROLLER_STOPPING

    def record_or_pause(self):
        if self.state == ControllerState.CONTROLLER_STOPPING:
            logging.info("start threading now")
            self.start_thread()
        else:
            self.recorder.switch()

    def input_human_message(self, msg):
        self.gpt_bridge.put(msg)

    # 绑定whisper speech to text 后的结果，后触发信号的callback
    def bind_stt_message_trigger(self, callback):
        self.stt_processor.set_callback(callback)

    # 绑定 gpt response到达后的callback函数
    def bind_gpt_message_trigger(self, callback):
        self.gpt_bridge.set_callback(callback)

    # gpt 相关属性直接调用 GPTRequestor，不单独封装
    def set_attributes_speaker(self, speaker_speed=None, speaker_voice=None):
        self.speaker.set_attributes(speaker_speed, speaker_voice)
    
    def set_attributes_stt(self, stt_model_name=None, stt_language=None):
        self.stt_processor.set_attributes(stt_model_name, stt_language)

    def set_attributes_recorder(self, recorder_input_device):
        self.recorder.select_device(recorder_input_device)

    def pause_speaking(self):
        self.speaker.pause()



    
