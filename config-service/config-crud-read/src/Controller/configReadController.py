from fastapi import APIRouter, HTTPException
from src.config.db import get_connection

router = APIRouter()

@router.get("/configs/{key_name}")
def get_config(key_name: str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM configurations WHERE key_name = %s"
    
    cursor.execute(query, (key_name,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail="Config not found")
