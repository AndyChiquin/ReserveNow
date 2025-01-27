from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.table import Table
from app.database import get_db

router = APIRouter(prefix="/tables", tags=["Delete"])

@router.delete("/{table_id}")
def delete_table(table_id: int, db: Session = Depends(get_db)):
    table = db.query(Table).filter(Table.id == table_id).first()
    if not table:
        raise HTTPException(status_code=404, detail="Table not found")
    db.delete(table)
    db.commit()
    return {"message": "Table deleted successfully"}
