class BaseException(Exception):
    message = ""

    def __init__(self, message=None, *args: object) -> None:
        if message:
            self.message += (":" + message)
        super().__init__(*args)


class DeviceNotSelectedError(BaseException):
    message = u"设备未选择"

class AITranscribeError(BaseException):
    message = u"语音转文字失败"

class GPTRequestorError(BaseException):
    message = u"GPT请求失败"

class FileWriteError(BaseException):
    message = u"文件写入失败"

class FileReadError(BaseException):
    message = u"文件读取失败"