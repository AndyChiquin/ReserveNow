from sqlalchemy import Column, Integer, String
from app.config import Base
from pydantic import BaseModel

class Configuration(Base):
    __tablename__ = "configurations"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String(255), unique=True, nullable=False)
    value = Column(String, nullable=False)
    description = Column(String, nullable=True)

class Config(BaseModel):
    key: str
    value: str
    description: str = None
