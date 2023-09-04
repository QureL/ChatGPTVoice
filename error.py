class BaseException(Exception):
    message = ""
    def __init__(self, message, *args: object) -> None:
        self.message += message
        super().__init__(*args)

class DeviceNotSelected(BaseException):
    message = u"设备未选择"

