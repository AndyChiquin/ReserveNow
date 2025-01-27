from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Table(Base):
    __tablename__ = "tables"

    id = Column(Integer, primary_key=True, index=True)
    table_number = Column(Integer, unique=True, nullable=False)
    capacity = Column(Integer, nullable=False)
    status = Column(Enum("available", "occupied", "reserved", name="status_enum"), default="available")
