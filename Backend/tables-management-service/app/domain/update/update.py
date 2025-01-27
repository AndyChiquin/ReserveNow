from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.table import Table
from app.database import get_db

router = APIRouter(prefix="/tables", tags=["Update"])

@router.put("/{table_id}")
def update_table(table_id: int, status: str, db: Session = Depends(get_db)):
    table = db.query(Table).filter(Table.id == table_id).first()
    if not table:
        raise HTTPException(status_code=404, detail="Table not found")
    table.status = status
    db.commit()
    db.refresh(table)
    return table
