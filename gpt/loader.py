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

def rename_session(session_name, new_name):
    pass
