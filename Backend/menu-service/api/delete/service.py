from db.database import get_connection

def delete_menu(menu_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM menus WHERE id=?", (menu_id,))
    conn.commit()
    conn.close()
    return {"message": "Menu deleted successfully"}
