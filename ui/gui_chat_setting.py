
from ui.design.Ui_gpt_setting import Ui_GPT_Setting
from PySide6.QtWidgets import QWidget
from config.config_json import load_config
from gpt.gpt import GPTReuqestor
from controller.gpt_chat_controller import GPTChatController
from config.const import *
class GPTSettingWindow(QWidget, Ui_GPT_Setting):

    def __init__(self, parent: QWidget ) -> None:
        super().__init__()
        self.setupUi(self)
        self.parent = parent

        self.render_ui()
        self.bind_buttons()

    # todo : 每次open都应该重写渲染
    def render_ui(self):
        config = load_config()
        self.spinBox_context_cnt.setValue(config.gpt_context_cnt)
        self.textEdit_system_cmd.setPlainText(config.gpt_sys_cmd)
        self.doubleSpinBox_speak_speed.setValue(config.speaker_speed)
        self.lineEdit_api_base.setText(config.openai_api_base)
        self.lineEdit_api_key.setText(config.openai_api_key)
        self.doubleSpinBox_temperature.setValue(config.gpt_temperature)

    def bind_buttons(self):
        gpt_requestor = GPTReuqestor.get_instance()
        controller = GPTChatController.get_instance()
        def confirm_callback():
            gpt_requestor.set_attributes(
                openai_api_base=self.lineEdit_api_base.text(),
                openai_api_key=self.lineEdit_api_key.text(),
                gpt_context_cnt=self.spinBox_context_cnt.value(),
                gpt_temperature=self.doubleSpinBox_temperature.value(),
            )
            gpt_requestor.set_system_command(self.textEdit_system_cmd.toPlainText())
            controller.set_attributes_speaker(
                speaker_speed=self.doubleSpinBox_speak_speed.value()
            )

            self.close()

        self.btn_confirm.clicked.connect(confirm_callback)

        self.btn_cancel.clicked.connect(self.close)





