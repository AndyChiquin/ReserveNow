from fastapi import APIRouter, HTTPException
from src.config.db import get_connection

router = APIRouter()

@router.delete("/configs/{key_name}")
def delete_config(key_name: str):
    conn = get_connection()
    cursor = conn.cursor()

    # Check if the configuration exists before deleting
    check_query = "SELECT COUNT(*) FROM configurations WHERE key_name = %s"
    cursor.execute(check_query, (key_name,))
    exists = cursor.fetchone()[0]

    if exists == 0:
        raise HTTPException(status_code=404, detail="❌ Config not found")

    # Delete the configuration
    delete_query = "DELETE FROM configurations WHERE key_name = %s"
    try:
        cursor.execute(delete_query, (key_name,))
        conn.commit()

        return {"message": "✅ Config deleted successfully", "key_name": key_name}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"❌ Database error: {str(e)}")
    finally:
        cursor.close()
        conn.close()
