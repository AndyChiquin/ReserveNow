from pydantic import BaseModel

class ConfigModel(BaseModel):
    key_name: str
    value: str
