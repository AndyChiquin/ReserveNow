from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.models.table import Table
from app.database import get_db
from app.config.settings import settings

router = APIRouter(prefix="/tables", tags=["Create"])

class CreateTable(BaseModel):
    table_number: int
    capacity: int

def check_existing_table(table_number: int, db: Session):
    """✅ SRP: Function responsible only for checking if a table already exists."""
    existing_table = db.query(Table).filter(Table.table_number == table_number).first()
    return existing_table

def create_new_table(request: CreateTable, db: Session):
    """✅ SRP: Function responsible only for creating a new table."""
    new_table = Table(table_number=request.table_number, capacity=request.capacity)
    db.add(new_table)
    db.commit()
    db.refresh(new_table)
    return new_table

@router.post("/")
def create_table(request: CreateTable, db: Session = Depends(get_db)):
    """✅ SRP: Main function now delegates responsibilities to specific functions."""
    existing_table = check_existing_table(request.table_number, db)  # ✅ SRP: Check if the table already exists.
    if existing_table:
        raise HTTPException(status_code=400, detail="Table number already exists")

    new_table = create_new_table(request, db)  # ✅ SRP: Creating a new table.
    return {"message": "Table created", "table": new_table}

@router.post("/assign", tags=["Assign"])
def assign_table(capacity: int, db: Session = Depends(get_db)):
    """✅ SRP: Function for assigning a table with enough capacity."""
    table = db.query(Table).filter(Table.status == "available", Table.capacity >= capacity).first()
    if not table:
        raise HTTPException(status_code=404, detail="No available table found")

    table.status = "reserved"
    db.commit()
    db.refresh(table)
    return {"message": "Table assigned", "table": table}
