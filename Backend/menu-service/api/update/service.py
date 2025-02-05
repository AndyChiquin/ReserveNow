from db.database import get_connection

def update_menu(menu_id, name, description, status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE menus SET name=?, description=?, status=? WHERE id=?", (name, description, status, menu_id))
    conn.commit()
    conn.close()
    return {"message": "Menu updated successfully"}
