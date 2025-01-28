from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from typing import Optional
from app.models.table import Table
from app.database import get_db

router = APIRouter(prefix="/tables", tags=["Update"])

# Modelo para el cuerpo de la solicitud
class UpdateTableRequest(BaseModel):
    status: Optional[str] = Field(None, pattern="^(available|reserved|occupied)$", description="Status of the table")
    capacity: Optional[int] = Field(None, gt=0, description="Capacity of the table")

@router.put("/{table_id}")
def update_table(table_id: int, request: UpdateTableRequest, db: Session = Depends(get_db)):
    # Buscar la mesa
    table = db.query(Table).filter(Table.id == table_id).first()
    if not table:
        raise HTTPException(status_code=404, detail="Table not found")
    
    # Actualizar el estado y/o capacidad solo si se proporcionan
    if request.status is not None:
        table.status = request.status
    if request.capacity is not None:
        table.capacity = request.capacity
    
    db.commit()
    db.refresh(table)
    
    return {"message": "Table updated successfully", "table": table}
