from sqlalchemy.orm import Session
from app.db.models import Configuration

def create_config(db: Session, key: str, value: str, description: str = None):
    config = Configuration(key=key, value=value, description=description)
    db.add(config)
    db.commit()
    db.refresh(config)
    return config
