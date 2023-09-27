# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. 
# If a copy of the MPL was not distributed with this file, 
# You can obtain one at https://mozilla.org/MPL/2.0/.
#
# Author: qurel
# GitHub: https://github.com/QureL/horn
# Copyright reserved

from ui.design.Ui_gpt_session_select_window import Ui_gpt_session_select
from ui.design.Ui_gpt_session_show import Ui_gpt_show_session
from PySide6.QtWidgets import QWidget
from gpt.gpt import GPTReuqestor
from gpt.loader import display_history_sessions, load_messages, rename_session

class GPTShowSession(QWidget, Ui_gpt_show_session):
    def __init__(self,) -> None:
        super().__init__()
        self.setupUi(self)


class GPTSessionSelect(QWidget, Ui_gpt_session_select):

    def __init__(self, parent) -> None:
        super().__init__()
        self.setupUi(self)
        self.parent = parent

        self.listWidget.addItems(display_history_sessions())
        self._bind_btns()
        self.show_window = GPTShowSession()

    def _bind_btns(self):
        ##############################################
        def confirm_btn_callback():
            session = self.listWidget.currentItem().text()
            if session and len(session) > 0: 
                gpt_requstor = GPTReuqestor.get_instance()
                gpt_requstor.set_session(session)
            self.close()

        self.confirm_btn.clicked.connect(confirm_btn_callback)

        self.cancel_btn.clicked.connect(self.close)
        ##############################################
        def view_btn_callback():
            message = load_messages(self.listWidget.currentItem().text())
            self.show_window.show()
            for msg in message:
                self.show_window.textBrowser.append(msg.type + ":" + msg.content + '\n')

        self.view_btn.clicked.connect(view_btn_callback)
        ##############################################
        # todo 重命名会话
        def rename_btn_callback():
            from gpt.loader import root_path
            session_name = self.listWidget.currentItem().text()

    def closeEvent(self, event) -> None:
        self.show_window.close()