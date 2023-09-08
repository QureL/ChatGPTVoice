
from ui.design.Ui_gpt_setting import Ui_GPT_Setting
from PySide6.QtWidgets import QWidget
from config.config import GPTChatConfig
from config.const import *
class GPTSettingWindow(QWidget, Ui_GPT_Setting):

    def __init__(self, parent: QWidget ) -> None:
        super().__init__()
        self.setupUi(self)
        self.parent = parent

        self.config = GPTChatConfig()
        self.render_ui()
        self.bind_buttons()


    def render_ui(self):

        context_cnt = self.config.get_config(GPT_CONTEXT_CNT)
        if context_cnt != None:
            self.spinBox_context_cnt.setValue(int(context_cnt))
        
        system_cmd = self.config.get_config(GPT_SYSTEM_CMD)
        if system_cmd != None:
            self.textEdit_system_cmd.setPlainText(system_cmd)

        speed = self.config.get_config(GPT_SPEAK_SPEED)
        if speed != None:
            self.doubleSpinBox_speak_speed.setValue(float(speed))

    def bind_buttons(self):

        def confirm_callback():
            self.config.set_config(
                GPT_CONTEXT_CNT, self.spinBox_context_cnt.value()
            )
            self.config.set_config(
                GPT_SYSTEM_CMD, self.textEdit_system_cmd.toPlainText()
            )
            self.config.set_config(
                GPT_SPEAK_SPEED, self.doubleSpinBox_speak_speed.value()
            )
            self.close()
            self.parent.reload_setting()

        self.btn_confirm.clicked.connect(confirm_callback)

        self.btn_cancel.clicked.connect(self.close)





