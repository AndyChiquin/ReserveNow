import os
import mysql.connector
from dotenv import load_dotenv

# Cargar variables de entorno
env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../.env'))
if os.path.exists(env_path):
    load_dotenv(env_path)
else:
    raise FileNotFoundError("❌ ERROR: Archivo .env no encontrado.")

# Verificar que las variables se están cargando correctamente
print("🔍 Verificando variables de entorno...")
for var in ["DB_HOST", "DB_USER", "DB_PASSWORD", "DB_NAME", "DB_PORT"]:
    value = os.getenv(var)
    print(f"{var}: {'NO DEFINIDO' if value is None else value}")

# Función para conectar con MySQL
def get_connection():
    try:
        print("🔄 Intentando conectar a MySQL en AWS...")
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=int(os.getenv("DB_PORT", 3306)),
            use_pure=True
        )
        print("✅ Conexión exitosa a MySQL en AWS.")
        return conn
    except mysql.connector.Error as err:
        print(f"❌ ERROR de conexión a MySQL: {err}")
        raise err
