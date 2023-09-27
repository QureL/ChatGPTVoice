# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. 
# If a copy of the MPL was not distributed with this file, 
# You can obtain one at https://mozilla.org/MPL/2.0/.
#
# Author: qurel
# GitHub: https://github.com/QureL/horn
# Copyright reserved

import pyaudio
import error
import logging
from config.config_json import load_config
from PySide6.QtCore import QThread, QMutex, QTimer
from queue import Queue

S2T_RATE = 16000 
T2S_RATE = 24_000 # 帧率可以调节语速
RATE = 16000
CHANNELS = 1
CHUNK = 1024
FORMAT = pyaudio.paInt16


class AudioDeviceKeepr:

    def __init__(self) -> None:
        self.p = pyaudio.PyAudio()
        self.devices = {}
        self.__build_device_list()
    
    __instance = None
    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = AudioDeviceKeepr()
        return cls.__instance

    def __build_device_list(self):
        for i in range(self.p.get_device_count()):
            devInfo = self.p.get_device_info_by_index(i)
            if devInfo['hostApi'] == 0:
                self.devices[i] = devInfo

    def display_devices(self, input=None):
        if input is None:
            return [ v['name'] for v in self.devices.values()]
        elif input == True:
            ret = []
            for v in self.devices.values():
                if v['maxInputChannels'] > 0: ret.append(v['name'])
        else:
            ret = []
            for v in self.devices.values():
                if v['maxOutputChannels'] > 0: ret.append(v['name'])
        return ret

    def get_device_index(self, device_name):
        for index, value in self.devices.items():
            if device_name == value['name']:
                return index


class AudioSpeaker(QThread):
    __instance = None

    def __init__(self, keeper: AudioDeviceKeepr, speed=1) -> None:
        self.keeper = keeper
        self.q = Queue()
        self._running = True
        self.device_index = None
        self.speed = speed
        self.stream = None
        self.rate = int(T2S_RATE*self.speed)
        self._speaking = True
        self._last_speech = None
        super().__init__()

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = AudioSpeaker(AudioDeviceKeepr.get_instance())
        return cls.__instance

    # must called before start!
    def select_device(self, device_name):
        self.device_index = self.keeper.get_device_index(device_name)

    def run(self) -> None:
        if self.device_index is None:
            raise error.DeviceNotSelectedError()
        self.stream = self.keeper.p.open(input_device_index=self.device_index,
                                            format=FORMAT,
                                            channels=CHANNELS,
                                            rate=self.rate,
                                            output=True,
                                            frames_per_buffer=CHUNK)
        while self._running:
            data = self.q.get()
            self._last_speech = data
            cnt = 0
            while self._speaking:
                data_per_sec = data[cnt*self.rate:(cnt+1)*self.rate]
                if len(data_per_sec) == 0: break
                cnt += 1
                self.stream.write(data_per_sec)
        self.stream.stop_stream()
        self.stream.close()

    def put(self, audio):
        self.q.put(audio)

    def stop(self):
        self._running = False

    def speak_again(self):
        if self._last_speech is not None:
            self.put(self._last_speech)

    def pause(self):
        self._speaking = not self._speaking

class AudioRecorder(QThread):
    mutex = QMutex()

    def __init__(self, keeper: AudioDeviceKeepr, 
                 output_pipe, 
                 is_chat: bool,
                 secs: int) -> None:
        self.keeper = keeper
        self.q = Queue()
        self._running = True
        self.device_index = None
        self.output_pipe = output_pipe
        self.is_chat_mode = is_chat
        self.cond_q = Queue()
        self._frames = []
        self._has_recorded = False

        if not self.is_chat_mode:
            self.timer = QTimer()
            self.timer.timeout.connect(self.timer_callback)
            self.secs = secs

        super().__init__()

    def timer_callback(self):
        logging.info("recorder timer callback trigger")
        self.cond_q.put(0)

    def select_device(self, device_name):
        self.device_index = self.keeper.get_device_index(device_name)

    def start_timer(self):
        logging.info("recorder`s timer start..., seconds=%d", self.secs)
        if not self.is_chat_mode: self.timer.start(self.secs*1000)

    def run(self) -> None:
        if self.device_index is None:
            raise error.DeviceNotSelectedError()
        self._has_recorded = True
        logging.info("self.device_index=%d", self.device_index)
        stream = self.keeper.p.open(input_device_index=self.device_index,
                                    format=FORMAT,
                                    channels=CHANNELS,
                                    rate=S2T_RATE,
                                    input=True,
                                    frames_per_buffer=CHUNK)
        #if not self.is_chat_mode: self.timer.start(self.secs)
        while self._running:
            if self.is_chat_mode:
                self.mutex.lock()
                self.mutex.unlock()
            else:
                if not self.cond_q.empty():
                    self.cond_q.get()
                    logging.info("recorder send to pipe...")
                    self.output_pipe.put(b''.join(self._frames))
                    self._frames.clear()

            data = stream.read(CHUNK)
            self._frames.append(data)

    def record(self):
        return self.q.get()

    def stop(self):
        logging.debug("Recorder stop...")
        self._running = False

    def switch(self):
        if self._has_recorded:
            self.mutex.lock()
            self._has_recorded = False
            # todo: send recorded audio
            if len(self._frames) > 0:
                self.output_pipe.put(b''.join(self._frames))
                self._frames.clear()
        else:
            self.mutex.unlock()
            self._has_recorded = True

