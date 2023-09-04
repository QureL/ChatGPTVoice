from ui.design.Ui_setting import Ui_setting_window
from PySide6.QtWidgets import QWidget
from config.config import SubtitleConfig, GPTChatConfig
from config.const import *


class SettingWindow(QWidget, Ui_setting_window):

    def __init__(self, ) -> None:
        super().__init__()
        self.setupUi(self)
        self.subtitle_config = SubtitleConfig()
        subtitle_sample_time = self.subtitle_config.get_config(SAMPLE_TIME)
        if not subtitle_sample_time:
            self.subtitle_config.set_config(SAMPLE_TIME, 10)

        ai_mode = self.subtitle_config.get_config(SUBTITLE_AI_MODE)
        if not ai_mode:
            self.subtitle_config.set_config(SUBTITLE_AI_MODE, 0)

        self.render_config_subtilte()
        self.render_config_gpt()

    def render_config_subtilte(self):

        self.subtitle_sample_time.setValue(
            int(self.subtitle_config.get_config(SAMPLE_TIME)))
        self.subtitle_mode_select_combo.setCurrentIndex(
            int(self.subtitle_config.get_config(SUBTITLE_AI_MODE)))
        self.subtitle_remote_address.setText(
            '' if not self.subtitle_config.get_config(REMOTE_ADDRESS) else self
            .subtitle_config.get_config(REMOTE_ADDRESS))
        self.subtitle_remote_address.setEnabled(
            self.subtitle_mode_select_combo.currentIndex() != 0)

        def mode_select_mode_callback():
            if self.subtitle_mode_select_combo.currentIndex() == 0:
                self.subtitle_remote_address.setEnabled(False)
            else:
                self.subtitle_remote_address.setEnabled(True)

        self.subtitle_mode_select_combo.currentIndexChanged.connect(
            mode_select_mode_callback)

        def confirm_callback():
            self.subtitle_config.set_config(SAMPLE_TIME,
                                            self.subtitle_sample_time.value())
            self.subtitle_config.set_config(
                SUBTITLE_AI_MODE,
                self.subtitle_mode_select_combo.currentIndex())
            self.subtitle_config.set_config(
                REMOTE_ADDRESS, self.subtitle_remote_address.text())
            self.close()

        self.subtitle_confirm.clicked.connect(confirm_callback)

        self.subtitle_setting_cancel.clicked.connect(self.close)

    def render_config_gpt(self):
        gpt_config = GPTChatConfig()
        self.line_edit_api_base.setText(gpt_config.get_config(OPENAI_API_BASE))
        self.line_edit_api_key.setText(gpt_config.get_config(OPENAI_API_KEY))

        speed = gpt_config.get_config(GPT_SPEAK_SPEED)
        if speed != None:
            self.spin_box_speak_speed.setValue(int(speed))

        context_cnt = gpt_config.get_config(GPT_CONTEXT_CNT)
        if context_cnt != None:
            self.spin_box_context_cnt.setValue(int(context_cnt))

        s2t_mode = gpt_config.get_config(GPT_S2T_MODE)
        if s2t_mode != None:
            self.combo_box_s2t_mode.setCurrentIndex(int(s2t_mode))

        t2s_mode = gpt_config.get_config(GPT_T2S_MODE)
        if t2s_mode != None:
            self.combox_box_t2s_mode.setCurrentIndex(int(t2s_mode))

        self.line_edit_s2t_remote_address.setText(gpt_config.get_config(GPT_S2T_REMOTE_ADDRESS))
        self.line_edit_t2s_remote_address.setText(gpt_config.get_config(GPT_T2S_REMOTE_ADDRESS))

        self.line_edit_s2t_remote_address.setEnabled(
            self.combo_box_s2t_mode.currentIndex() != 0)
        self.line_edit_t2s_remote_address.setEnabled(
            self.combox_box_t2s_mode.currentIndex() != 0)

        self.combo_box_s2t_mode.currentIndexChanged.connect(
            lambda: self.line_edit_s2t_remote_address.setEnabled(
                self.combo_box_s2t_mode.currentIndex() != 0))

        self.combox_box_t2s_mode.currentIndexChanged.connect(
            lambda: self.line_edit_t2s_remote_address.setEnabled(
                self.combox_box_t2s_mode.currentIndex() != 0))
        
        self.btn_gpt_setting_cancel.clicked.connect(self.close)

        def confirm_callback():
            gpt_config.set_config(OPENAI_API_BASE, self.line_edit_api_base.text())
            gpt_config.set_config(OPENAI_API_KEY, self.line_edit_api_key.text())

            gpt_config.set_config(GPT_CONTEXT_CNT, self.spin_box_context_cnt.value())
            gpt_config.set_config(GPT_SPEAK_SPEED, self.spin_box_speak_speed.value())

            gpt_config.set_config(GPT_T2S_MODE, self.combo_box_s2t_mode.currentIndex())
            gpt_config.set_config(GPT_S2T_MODE, self.combox_box_t2s_mode.currentIndex())

            gpt_config.set_config(GPT_S2T_REMOTE_ADDRESS, self.line_edit_s2t_remote_address.text())
            gpt_config.set_config(GPT_T2S_REMOTE_ADDRESS, self.line_edit_t2s_remote_address.text())

            self.close()

        self.btn_gpt_setting_confirm.clicked.connect(confirm_callback)




