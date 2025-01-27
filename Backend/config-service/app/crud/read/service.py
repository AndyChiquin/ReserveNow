from sqlalchemy.orm import Session
from app.db.models import Configuration

def get_config(db: Session, key: str):
    config = db.query(Configuration).filter(Configuration.key == key).first()
    if not config:
        raise ValueError(f"Configuration with key '{key}' not found")
    return config
