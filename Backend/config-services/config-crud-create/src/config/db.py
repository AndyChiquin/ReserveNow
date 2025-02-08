import os
import mysql.connector
from dotenv import load_dotenv

# Cargar variables de entorno
env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../.env'))
if os.path.exists(env_path):
    load_dotenv(env_path)
else:
    raise FileNotFoundError("❌ ERROR: Archivo .env no encontrado en la carpeta raíz")

# Verificar si las variables de entorno se cargan correctamente
print("🔍 Verificando variables de entorno...")
for var in ["DB_HOST", "DB_USER", "DB_PASSWORD", "DB_NAME", "DB_PORT"]:
    print(f"{var}: {os.getenv(var)}")

# Función para conectar con MySQL
def get_connection():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=int(os.getenv("DB_PORT")),
            use_pure=True
        )
        print("✅ Conexión exitosa a MySQL")
        return conn
    except mysql.connector.Error as err:
        print(f"❌ ERROR de conexión a MySQL: {err}")
        raise err

# Ejecutar prueba de conexión
if __name__ == "__main__":
    try:
        conn = get_connection()
        conn.close()
    except Exception as e:
        print(f"❌ ERROR en la conexión: {e}")
