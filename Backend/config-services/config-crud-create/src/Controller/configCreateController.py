from fastapi import APIRouter, HTTPException, Depends
from src.config.db import get_connection
from src.Model.configModel import ConfigModel

router = APIRouter()

@router.post("/configs")
def create_config(config: ConfigModel):
    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO configurations (key_name, value) VALUES (%s, %s)"
    values = (config.key_name, config.value)

    try:
        cursor.execute(query, values)
        conn.commit()
        return {"message": "Config added successfully", "key_name": config.key_name}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    finally:
        cursor.close()
        conn.close()
