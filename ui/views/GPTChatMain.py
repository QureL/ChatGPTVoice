# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. 
# If a copy of the MPL was not distributed with this file, 
# You can obtain one at https://mozilla.org/MPL/2.0/.

from qfluentwidgets import FluentIcon, TextEdit, PushButton, ToolButton, PrimaryPushButton
from qframelesswindow import FramelessWindow
from PySide6.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QDesktopServices
from ui.component.ChatArea import ChatArea
from ui.component.ChatHistoryScroll import ChatHistoryScroll
from ui.component.IOSettingComponent import IOSettingComponent
from ui.component.TalkMicButton import TalkMicButton
from ui.component.VoiceControlButton import VoiceControlButton
from const import *
import logging, sys
from ui.gui_chat_setting import GPTSettingWindow
from gpt.gpt import GPTReuqestor
from gpt.loader import load_messages
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
from config.const import *

from PySide6.QtCore import Signal
from controller.gpt_chat_controller import GPTChatController
from config.config_json import dump_config


class GPTChatMain(FramelessWindow):
    text_browser_signal = Signal(str)
    correct_s2t_editor_signal = Signal(str)
    shall_correct_s2t = False

    def __init__(self, parent=None):
        super().__init__(parent)
        desktop = QApplication.primaryScreen().size()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)
        self.hBoxLayout = QHBoxLayout(self)

        # 渲染历史记录和聊天区域
        self.chatHistoryScroll = ChatHistoryScroll(self)
        self.chatArea = ChatArea(self)
        self.IOSetting = IOSettingComponent(self)
        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.setContentsMargins(0, 20, 0, 0)
        self.vBoxLayout.setSpacing(5)
        self.vBoxLayout.addWidget(self.IOSetting)
        # 设置按钮
        self.settingGithubButtonLayout = QHBoxLayout()
        self.settingButton = PushButton("setting", self, FluentIcon.SETTING)
        self.settingButton.setFixedWidth(95)
        # github
        self.github = ToolButton(FluentIcon.GITHUB, self)
        self.settingGithubButtonLayout.setSpacing(5)
        self.settingGithubButtonLayout.addWidget(self.settingButton, 0, Qt.AlignmentFlag.AlignLeft)
        self.settingGithubButtonLayout.addWidget(self.github, 0, Qt.AlignmentFlag.AlignLeft)
        self.settingGithubButtonLayout.addSpacing(300)
        # 禁声按钮
        self.vioceControlButton = VoiceControlButton(self)

        self.vBoxLayout.addLayout(self.settingGithubButtonLayout)
        self.vBoxLayout.addWidget(self.chatArea)

        self.hBoxLayout.addWidget(self.chatHistoryScroll)
        self.hBoxLayout.addLayout(self.vBoxLayout)

        # 渲染输入框
        self.inputTextEdit = TextEdit(self)
        self.inputTextEdit.setFixedHeight(100)
        # 开始讲话按钮
        self.talkButton = TalkMicButton(self)
        # 发送按钮
        self.sendButton = PrimaryPushButton("Send", self, FluentIcon.SEND)
        
        
        self.buttonVBoxLayout = QVBoxLayout()
        self.buttonVBoxLayout.setSpacing(2)
        self.buttonVBoxLayout.addWidget(self.talkButton)
        self.buttonVBoxLayout.addWidget(self.sendButton)
        self.buttonVBoxLayout.addWidget(self.vioceControlButton)
        self.inputTextEdit.setPlaceholderText(
            'Click `Talk` Button to Start, then Click `Send` Button to Send. Or Input Text Here Directly.'
        )
        self.inpuAreaLayout = QHBoxLayout()
        self.inpuAreaLayout.addWidget(self.inputTextEdit)
        self.inpuAreaLayout.addLayout(self.buttonVBoxLayout)
        self.inpuAreaLayout.setSpacing(5)
        self.vBoxLayout.addLayout(self.inpuAreaLayout)

        self.gpt_setting_window = GPTSettingWindow(self)
        self.controller = GPTChatController.get_instance()
        self.render_combo_boxes()
        self.bind_buttons()
        self.bind_signals()
        self.bind_controller_callback()

    def render_combo_boxes(self):
        self.IOSetting.commboxSelectInputDevice.addItems(self.controller.display_audio_input_devices())
        self.IOSetting.commboxSelectGPTOutputDevice.addItems(self.controller.display_audio_voices())

    def bind_buttons(self):
        #################################
        ####    Talk按钮绑定
        def start_btn_clicked_callback():
            self.update_configurations()
            self.controller.record_or_pause()
            self.talkButton.switch()
        self.talkButton.clicked.connect(start_btn_clicked_callback)
        #################################
        ####    发送按钮绑定
        def tab1_send_corrected_text_btn_callback():
            txt = self.inputTextEdit.toPlainText()
            if len(txt) == 0: return
            self.controller.input_human_message(txt)

            self.inputTextEdit.clear()
            self.chatArea.add_human_message(txt)
        self.sendButton.clicked.connect(tab1_send_corrected_text_btn_callback)

        #################################
        #### 设置按钮绑定
        def btn_gpt_setting_callback():
            self.gpt_setting_window.render_ui()
            self.gpt_setting_window.show()

        self.settingButton.clicked.connect(btn_gpt_setting_callback)
        #################################
        ####    禁声按钮绑定
        def voice_control_btn_callback():
            self.controller.pause_speaking()
            self.vioceControlButton.switch()
        self.vioceControlButton.clicked.connect(voice_control_btn_callback)
        #################################
        ####    github
        self.github.clicked.connect(lambda: 
            QDesktopServices.openUrl(QUrl("https://github.com/QureL/GPT_Talk_Local")))


    def bind_signals(self):
        #################################
        ####    gpt message signal 绑定
        self.text_browser_signal.connect(self.chatArea.add_bot_message)
        ####    whisper识别结果 signal 绑定
        self.correct_s2t_editor_signal.connect(self.inputTextEdit.append)

        #################################
        ####    选择历史记录后的回调
        def select_session_callback(session):
            gpt_requstor = GPTReuqestor.get_instance()
            gpt_requstor.set_session(session)
            message = load_messages(session)
            self.chatArea.clear_message()
            for msg in message:
                if msg.type == "human":
                    self.chatArea.add_human_message(msg.content)
                elif msg.type == "ai":
                    self.chatArea.add_bot_message(msg.content)
        self.chatHistoryScroll.selected_session_signal.connect(select_session_callback)

    # 提供给controller的页面修改回调
    def bind_controller_callback(self):
        self.controller.bind_stt_message_trigger(self.correct_s2t_editor_signal.emit)
        self.controller.bind_gpt_message_trigger(self.text_browser_signal.emit)


    # 配置speaker声音，recorder输入设备
    def update_configurations(self):
        input_device = self.IOSetting.commboxSelectInputDevice.currentText()
        output_voice = self.IOSetting.commboxSelectGPTOutputDevice.currentText()

        self.controller.set_attributes_speaker(speaker_voice=output_voice)
        self.controller.set_attributes_recorder(recorder_input_device=input_device)

    def release_resource(self):
        # 保存配置
        dump_config()
        self.controller.stop_thread()

    #################################
    ####    重写关闭事件
    def closeEvent(self, event):
        self.release_resource()
        event.accept()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = GPTChatMain()
    w.show()
    app.exec()


