from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.config import SessionLocal
from app.crud.read.service import get_config
from app.db.models import ConfigurationResponse
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

@router.get("/configs/{key}", response_model=ConfigurationResponse)
def read_config(key: str, db: Session = Depends(get_db)):
    try:
        # Consulta la clave en la base de datos
        config = db.query(Configuration).filter_by(key=key).first()
        if not config:
            raise HTTPException(
                status_code=404,
                detail=f"Configuration with key '{key}' not found"
            )
        return config
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Unexpected error occurred: {str(e)}"
        )
