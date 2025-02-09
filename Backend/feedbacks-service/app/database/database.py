import pyodbc
import os
from dotenv import load_dotenv

# Cargar variables desde el archivo .env
load_dotenv()

DB_SERVER = os.getenv("DB_SERVER")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = os.getenv("DB_PORT", "1433")

# Mostrar variables para depuración (opcional, puedes comentar estas líneas)
print(f"📌 Verificación de Variables:")
print(f"DB_SERVER: {DB_SERVER}")
print(f"DB_NAME: {DB_NAME}")
print(f"DB_USER: {DB_USER}")
print(f"DB_PORT: {DB_PORT}")

# Construcción de la cadena de conexión ODBC
CONNECTION_STRING = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={DB_SERVER},{DB_PORT};DATABASE={DB_NAME};UID={DB_USER};PWD={DB_PASSWORD}"

def get_connection():
    """Establece y retorna una conexión a la base de datos."""
    try:
        conn = pyodbc.connect(CONNECTION_STRING)
        print("✅ Conexión exitosa a la base de datos")
        return conn
    except Exception as e:
        print(f"❌ Error al conectar a la base de datos: {e}")
        return None

# Prueba de conexión si se ejecuta directamente
if __name__ == "__main__":
    get_connection()
