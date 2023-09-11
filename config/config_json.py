from pydantic import BaseModel, Field
import os
from typing import List
import const
from error import FileWriteError, FileReadError
import logging
config_base_path = os.path.join(os.path.expanduser("~"), 'AppData', 'Local', 
                                f'{const.APP_NAME}',
                                f'{const.APP_NAME}.json')


class Config(BaseModel):
    
    # tts
    tts_mode: str = Field(default="local")
    tts_remote_address: str = Field(default="")

    # gpt
    openai_api_base: str = Field(default="")
    openai_api_key: str = Field(default="")
    gpt_context_cnt: int = Field(default=10)
    gpt_sys_cmd: str = Field(default="")
    gpt_model_name: str = Field(default="gpt-3.5-turbo")
    gpt_model_list: List[str] = Field(default=["gpt-3.5-turbo"])
    gpt_temperature: float = Field(default=1.0)
    gpt_top_n: float = Field(default=1.5)

    # whisper
    stt_model_name: str = Field(default="base")
    stt_model_list: List[str] = Field(default=['tiny', 'base', 'large-v2'])
    stt_language: str = Field(default="")
    stt_language_list: List[str] = Field(default=['en', 'cn', 'jp'])
    stt_mode: str = Field(default="local")
    stt_remote_address: str = Field(default="")

    # audio
    speaker_speed: float = Field(default=1.0)
    recorder_input_device: str = Field(default="")
    speaker_output_device: str = Field(default="")
    speaker_voice: str = Field(default="")


c = None
def load_config():
    global c
    if c is None:
        if not os.path.exists(config_base_path):
            try:
                with open(config_base_path, mode='w') as f:
                    c = Config()
                    f.write(c.model_dump_json())
            except Exception as ex:
                logging.error(ex)
                raise FileWriteError(message="配置文件写入失败")
        else:
            try:
                with open(config_base_path, mode='r', encoding='utf-8') as f:
                    c = Config.model_validate_json(f.read())
            except Exception as ex:
                logging.error(ex)
                raise FileReadError(message="配置文件读取失败")
    return c

def dump_config():
    load_config()
    try:
        with open(config_base_path, mode='w') as f:
            f.write(c.model_dump_json())
    except Exception as ex:
        logging.error(ex)
        raise FileWriteError(message="配置文件写入失败")



