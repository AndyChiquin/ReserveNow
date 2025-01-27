from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.table import Table
from app.database import get_db
from fastapi import HTTPException


router = APIRouter(prefix="/tables")

@router.post("/", tags=["Create"])
def create_table(table_number: int, capacity: int, db: Session = Depends(get_db)):
    new_table = Table(table_number=table_number, capacity=capacity)
    db.add(new_table)
    db.commit()
    db.refresh(new_table)
    return new_table


@router.post("/assign", tags=["Assign"])
def assign_table(capacity: int, db: Session = Depends(get_db)):
    table = db.query(Table).filter(Table.status == "available", Table.capacity >= capacity).first()
    if not table:
        raise HTTPException(status_code=404, detail="No available table found")

    table.status = "reserved"
    db.commit()
    db.refresh(table)
    return table
