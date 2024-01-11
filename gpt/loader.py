# This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. 
# If a copy of the MPL was not distributed with this file, 
# You can obtain one at https://mozilla.org/MPL/2.0/.
#
# Author: qurel
# GitHub: https://github.com/QureL/horn
# Copyright reserved

from langchain.memory import FileChatMessageHistory
import os, const

root_path = os.path.join(
    os.path.expanduser("~"), 'AppData', 'Local', 
    f'{const.APP_NAME}',
    'data',
    'messages',
)
if not os.path.exists(root_path):
    os.makedirs(root_path)

def display_history_sessions():
    for root, _, fs in os.walk(root_path):
        if root == root_path:
            return fs


def load_messages(session_pool: str):
    path = os.path.join(root_path, session_pool)
    history = FileChatMessageHistory(path)
    return history.messages

def rename_session(old_name, new_name):
    path = os.path.join(root_path, old_name)
    new_path = os.path.join(root_path, new_name)
    os.rename(path, new_path)
