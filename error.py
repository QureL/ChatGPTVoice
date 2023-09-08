class BaseException(Exception):
    message = ""

    def __init__(self, message=None, *args: object) -> None:
        if message:
            self.message += (":" + message)
        super().__init__(*args)


class DeviceNotSelected(BaseException):
    message = u"设备未选择"

class AITranscribeError(BaseException):
    message = u"语音转文字失败"

class GPTRequestorError(BaseException):
    message = u"GPT请求失败"