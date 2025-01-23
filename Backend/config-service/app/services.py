from sqlalchemy.orm import Session
from app.models import Configuration

def create_config(db: Session, key: str, value: str, description: str = None):
    config = Configuration(key=key, value=value, description=description)
    db.add(config)
    db.commit()
    db.refresh(config)
    return config

def get_config(db: Session, key: str):
    return db.query(Configuration).filter(Configuration.key == key).first()

def delete_config(db: Session, key: str):
    config = db.query(Configuration).filter(Configuration.key == key).first()
    if config:
        db.delete(config)
        db.commit()
    return config
