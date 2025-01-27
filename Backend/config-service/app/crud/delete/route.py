from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.config import SessionLocal
from app.crud.delete.service import delete_config
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

@router.delete("/configs/{key}")
def remove_config(key: str, db: Session = Depends(get_db)):
    try:
        # Consulta si la clave existe
        config = db.query(Configuration).filter_by(key=key).first()
        if not config:
            raise HTTPException(
                status_code=404,
                detail=f"Configuration with key '{key}' not found"
            )
        db.delete(config)
        db.commit()
        return {"message": f"Configuration '{key}' deleted successfully"}
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Unexpected error occurred: {str(e)}"
        )
