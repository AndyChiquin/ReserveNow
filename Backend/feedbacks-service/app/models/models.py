from database import get_connection

def create_feedback_table():
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='feedbacks' AND xtype='U')
        CREATE TABLE feedbacks (
            id INT IDENTITY(1,1) PRIMARY KEY,
            user_id INT NOT NULL,
            restaurant_id INT NOT NULL,
            rating INT CHECK (rating BETWEEN 1 AND 5),
            comment TEXT,
            created_at DATETIME DEFAULT GETDATE()
        );
        """)
        conn.commit()
        cursor.close()
        conn.close()
