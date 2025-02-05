from db.database import get_connection

def get_menus():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM menus")
    menus = cursor.fetchall()
    conn.close()
    return [{"id": row[0], "name": row[1], "description": row[2], "status": row[3]} for row in menus]
