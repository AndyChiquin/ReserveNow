from sqlalchemy import Column, Integer, String
from app.db.config import Base
from pydantic import BaseModel, Field

# Modelo SQLAlchemy para la base de datos
class Configuration(Base):
    __tablename__ = "configurations"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String(255), unique=True, nullable=False)
    value = Column(String, nullable=False)
    description = Column(String, nullable=True)


# Modelos Pydantic para entrada y salida
class ConfigurationCreate(BaseModel):
    key: str = Field(..., max_length=255, regex=r"^[a-zA-Z0-9_\-]+$", description="Unique key for the configuration")
    value: str = Field(..., description="Value of the configuration")
    description: str | None = Field(None, max_length=500, description="Optional description of the configuration")


class ConfigurationResponse(BaseModel):
    id: int
    key: str
    value: str
    description: str | None

    class Config:
        orm_mode = True
