from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.models.table import Table
from app.database import get_db

router = APIRouter(prefix="/tables", tags=["Create"])

# Modelo para el cuerpo de la solicitud
class CreateTable(BaseModel):
    table_number: int
    capacity: int


@router.post("/")
def create_table(request: CreateTable, db: Session = Depends(get_db)):
    # Verificar si el número de mesa ya existe
    existing_table = db.query(Table).filter(Table.table_number == request.table_number).first()
    if existing_table:
        raise HTTPException(status_code=400, detail="Table number already exists")

    # Crear la nueva mesa
    new_table = Table(table_number=request.table_number, capacity=request.capacity)
    db.add(new_table)
    db.commit()
    db.refresh(new_table)
    return {"message": "Table created", "table": new_table}

@router.post("/assign", tags=["Assign"])
def assign_table(capacity: int, db: Session = Depends(get_db)):
    # Buscar una mesa disponible con la capacidad requerida
    table = db.query(Table).filter(Table.status == "available", Table.capacity >= capacity).first()
    if not table:
        raise HTTPException(status_code=404, detail="No available table found")

    # Asignar la mesa
    table.status = "reserved"
    db.commit()
    db.refresh(table)
    return {"message": "Table assigned", "table": table}
