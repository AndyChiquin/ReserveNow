import os
import mysql.connector
from dotenv import load_dotenv

# Load environment variables
env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../.env'))
if os.path.exists(env_path):
    load_dotenv(env_path)
else:
    raise FileNotFoundError("❌ ERROR: .env file not found.")

# Verificar que las variables se están cargando correctamente
print("🔍 Checking environment variables...")
for var in ["DB_HOST", "DB_USER", "DB_PASSWORD", "DB_NAME", "DB_PORT"]:
    value = os.getenv(var)
    print(f"{var}: {'NO DEFINIDO' if value is None else value}")

# Function to connect with MySQL
def get_connection():
    try:
        print("🔄 Trying to connect to MySQL on AWS...")
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=int(os.getenv("DB_PORT", 3306)),
            use_pure=True
        )
        print("✅ Successful connection to MySQL on AWS.")
        return conn
    except mysql.connector.Error as err:
        print(f"❌ MySQL connection ERROR: {err}")
        raise err
