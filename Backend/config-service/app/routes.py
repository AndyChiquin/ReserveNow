from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config import SessionLocal
from app.services import create_config, get_config, delete_config
from app.models import Config

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/configs/")
def add_config(config: Config, db: Session = Depends(get_db)):
    return create_config(db, config.key, config.value, config.description)

@router.get("/configs/{key}")
def read_config(key: str, db: Session = Depends(get_db)):
    config = get_config(db, key)
    if not config:
        raise HTTPException(status_code=404, detail="Config not found")
    return config

@router.delete("/configs/{key}")
def remove_config(key: str, db: Session = Depends(get_db)):
    config = delete_config(db, key)
    if not config:
        raise HTTPException(status_code=404, detail="Config not found")
    return {"message": f"Config '{key}' deleted successfully"}
