from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.table import Table
from app.database import get_db
from app.config.settings import settings

router = APIRouter(prefix="/tables", tags=["Read"])

def serialize_table(table):
    """✅ DRY: Function to convert a table object to a dictionary."""
    return {
        "id": table.id,
        "table_number": table.table_number,
        "capacity": table.capacity,
        "status": table.status
    }

@router.get("/")
def get_tables(db: Session = Depends(get_db)):
    """✅ DRY: Return all tables using the serialization function."""
    tables = db.query(Table).all()
    return [serialize_table(table) for table in tables]  # ✅ DRY: Reusing the serialization function.

@router.get("/available", tags=["Read"])
def get_available_tables(db: Session = Depends(get_db)):
    """✅ DRY: Return only available tables using the serialization function."""
    available_tables = db.query(Table).filter(Table.status == "available").all()
    return [serialize_table(table) for table in available_tables]  # ✅ DRY: Reusing the serialization function.

@router.get("/{table_id}")
def get_table_by_id(table_id: int, db: Session = Depends(get_db)):
    """✅ DRY: Return a single table by ID using the serialization function."""
    table = db.query(Table).filter(Table.id == table_id).first()
    if not table:
        raise HTTPException(status_code=404, detail="Table not found")
    return serialize_table(table)  # ✅ DRY: Reusing the serialization function.
