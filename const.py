import enum


class Mode(enum.Enum):
    MODE_CHAT = 0
    MODE_SUBTITLE = 1


APP_NAME = "horn"

class ModelSize(enum.Enum):
    TINY = "tiny"
    MEDIUM = "base"
    LARGE = "large-v2"

class Language(enum.Enum):
    Default = '自动识别'
    English = 'English'
    Chinese = 'Chinese'
    Japanese = 'Japanese'
    
