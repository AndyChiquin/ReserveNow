import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

def get_db_connection():
    import mysql.connector
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            return connection
    except mysql.connector.Error as err:
        print(f"Error de conexión: {err}")
        return None
