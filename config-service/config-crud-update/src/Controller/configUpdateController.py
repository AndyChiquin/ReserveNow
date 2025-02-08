from fastapi import APIRouter, HTTPException, Depends
from src.config.db import get_connection
from src.Model.configModel import ConfigModel

router = APIRouter()

@router.put("/configs")
def update_config(config: ConfigModel):
    conn = get_connection()
    cursor = conn.cursor()

    # Check if the configuration exists before updating
    check_query = "SELECT COUNT(*) FROM configurations WHERE key_name = %s"
    cursor.execute(check_query, (config.key_name,))
    exists = cursor.fetchone()[0]

    if exists == 0:
        raise HTTPException(status_code=404, detail="❌ Config not found")

    # Update Configuration
    query = "UPDATE configurations SET value = %s WHERE key_name = %s"
    try:
        cursor.execute(query, (config.value, config.key_name))
        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=400, detail="❌ No changes made")

        return {"message": "✅ Config updated successfully", "key_name": config.key_name, "new_value": config.value}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"❌ Database error: {str(e)}")
    finally:
        cursor.close()
        conn.close()
