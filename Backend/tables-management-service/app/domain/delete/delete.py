from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.table import Table
from app.database import get_db
from app.config.settings import settings

router = APIRouter(prefix="/tables", tags=["Delete"])

def find_table_by_id(table_id: int, db: Session):
    """✅ SRP: Function responsible only for querying a table by ID."""
    return db.query(Table).filter(Table.id == table_id).first()

def delete_table_from_db(table, db: Session):
    """✅ SRP: Function responsible only for deleting a table from the database."""
    db.delete(table)
    db.commit()

@router.delete("/{table_id}")
def delete_table(table_id: int, db: Session = Depends(get_db)):
    """✅ SRP: Main function now delegates responsibilities to specific functions."""
    table = find_table_by_id(table_id, db)  # ✅ SRP: Find the table.
    
    if not table:
        raise HTTPException(status_code=404, detail="Table not found")

    delete_table_from_db(table, db)  # ✅ SRP: Delete the table.

    return {"message": "Table deleted successfully"}
