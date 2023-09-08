
from ui.design.Ui_gpt_setting import Ui_GPT_Setting
from PySide6.QtWidgets import QWidget
from config.config import GPTChatConfig
from config.const import *
class GPTSettingWindow(QWidget, Ui_GPT_Setting):

    def __init__(self, parent: QWidget ) -> None:
        super().__init__(parent,)
        self.setupUi(self)

        self.config = GPTChatConfig()


    def render_ui(self):

        context_cnt = self.config.get_config(GPT_CONTEXT_CNT)
        if context_cnt != None:
            self.spinBox_context_cnt.setValue(int(context_cnt))
        
        system_cmd = self.config.get_config(GPT_SYSTEM_CMD)
        if system_cmd != None:
            self.textEdit_system_cmd.setPlainText(system_cmd)

    def bind_buttons(self):

        def confirm_callback():
            self.config.set_config(
                GPT_CONTEXT_CNT, self.spinBox_context_cnt.value()
            )
            self.config.set_config(
                GPT_SYSTEM_CMD, self.textEdit_system_cmd.toPlainText()
            )

        self.btn_confirm.clicked.connect(confirm_callback)

        self.btn_cancel.clicked.connect(self.close)





