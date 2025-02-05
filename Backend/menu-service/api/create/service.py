from db.database import get_connection

def create_menu(name, description, status):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO menus (name, description, status) VALUES (?, ?, ?)", (name, description, status))
    conn.commit()
    conn.close()
    return {"message": "Menu created successfully"}
