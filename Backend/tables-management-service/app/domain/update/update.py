from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from typing import Optional
from app.models.table import Table
from app.database import get_db
from app.config.settings import settings

router = APIRouter(prefix="/tables", tags=["Update"])

class UpdateTableRequest(BaseModel):
    status: Optional[str] = Field(None, pattern="^(available|reserved|occupied)$", description="Status of the table")
    capacity: Optional[int] = Field(None, gt=0, description="Capacity of the table")

def update_table_fields(table, request: UpdateTableRequest):
    """✅ OCP: Function responsible only for updating the fields of the table."""
    if request.status is not None:
        table.status = request.status
    if request.capacity is not None:
        table.capacity = request.capacity

@router.put("/{table_id}")
def update_table(table_id: int, request: UpdateTableRequest, db: Session = Depends(get_db)):
    """✅ OCP: Main function now delegates responsibilities to specific functions."""
    table = db.query(Table).filter(Table.id == table_id).first()
    if not table:
        raise HTTPException(status_code=404, detail="Table not found")
    
    # ✅ OCP: Delegating table field updates to a separate function.
    update_table_fields(table, request)
    
    db.commit()
    db.refresh(table)
    
    return {"message": "Table updated successfully", "table": table}
