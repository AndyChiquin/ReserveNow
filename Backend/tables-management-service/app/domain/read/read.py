from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.table import Table
from app.database import get_db

router = APIRouter(prefix="/tables", tags=["Read"])

@router.get("/")
def get_tables(db: Session = Depends(get_db)):
    return db.query(Table).all()

@router.get("/available", tags=["Read"])
def get_available_tables(db: Session = Depends(get_db)):
    mesas = db.query(Table).filter(Table.status == "available").all()
    return [{"id": mesa.id, "table_number": mesa.table_number, "capacity": mesa.capacity, "status": mesa.status} for mesa in mesas]


@router.get("/{table_id}")
def get_table_by_id(table_id: int, db: Session = Depends(get_db)):
    table = db.query(Table).filter(Table.id == table_id).first()
    if not table:
        raise HTTPException(status_code=404, detail="Table not found")
    return table



