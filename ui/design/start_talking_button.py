from PySide6.QtWidgets import QPushButton

STATE_STOPPING = 0
STATE_RECORDING = 1
class start_talking_button(QPushButton):

    state = STATE_RECORDING

    