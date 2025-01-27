from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.config import SessionLocal
from app.crud.create.service import create_config
from app.db.models import ConfigurationCreate, ConfigurationResponse
from app.db.models import Configuration

# Inicializa el objeto APIRouter
router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/configs/", response_model=ConfigurationResponse)
def add_config(config: ConfigurationCreate, db: Session = Depends(get_db)):
    try:
        # Verifica si la clave ya existe
        existing_config = db.query(Configuration).filter_by(key=config.key).first()
        if existing_config:
            raise HTTPException(
                status_code=400,
                detail=f"Configuration with key '{config.key}' already exists"
            )
        return create_config(db, config.key, config.value, config.description)
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Unexpected error occurred: {str(e)}"
        )
