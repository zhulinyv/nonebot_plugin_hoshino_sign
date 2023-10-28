import os
from nonebot import get_driver
from pydantic import BaseModel, Extra

class Config(BaseModel, extra=Extra.ignore):
    stamp_path: str = os.path.join(os.path.dirname(__file__), "stamp")

sign_config = Config.parse_obj(get_driver().config.dict())
