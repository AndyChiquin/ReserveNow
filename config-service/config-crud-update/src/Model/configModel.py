from pydantic import BaseModel, Field

class ConfigModel(BaseModel):
    key_name: str = Field(..., min_length=3, max_length=255, description="Unique key identifier for the configuration")
    value: str = Field(..., min_length=1, description="Value of the configuration")
