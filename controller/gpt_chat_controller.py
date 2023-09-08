from controller.controller import Controller
from audio.audio import AudioDeviceKeepr
from audio.speaker_windows import SpeakderPyTTSx3
from config.config import GPTChatConfig

class GPTChatController():

    def __init__(self, speaker_speed=1) -> None:
        self.audio_device_keeper = AudioDeviceKeepr()
        self.speaker = SpeakderPyTTSx3(speaker_speed)
        
    
    def set_gpt_system_command(self, cmd):
        pass

    def display_audio_input_devices(self):
        return self.audio_device_keeper.display_devices(input=True)

    def display_audio_output_devices(self):
        return self.speaker.show_voices()

    def start_thread(self):
        pass

    def stop_thread(self):
        pass

    def record(self):
        pass

    def input_human_message(self):
        pass

    def bind_stt_message_trigger(self, callback):
        pass

    def bind_gpt_message_trigger(self, callback):
        pass


    def set_attribute(self, **args):
        pass