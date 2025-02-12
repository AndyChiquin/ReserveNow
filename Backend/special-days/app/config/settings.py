import os
import psycopg2
from dotenv import load_dotenv

# Cargar las variables de entorno desde .env
load_dotenv()

class Config:
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST")  # Aquí va el endpoint de AWS
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")

    # URI de conexión para SQLAlchemy
    SQLALCHEMY_DATABASE_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def test_db_connection():
        """Prueba la conexión con la base de datos en AWS RDS"""
        try:
            conn = psycopg2.connect(
                dbname=Config.POSTGRES_DB,
                user=Config.POSTGRES_USER,
                password=Config.POSTGRES_PASSWORD,
                host=Config.POSTGRES_HOST,
                port=Config.POSTGRES_PORT
            )
            conn.close()
            print("✅ Conexión a la base de datos AWS RDS establecida correctamente.")
        except Exception as e:
            print(f"❌ Error al conectar con la base de datos AWS RDS: {e}")

# Probar conexión al importar `Config`
Config.test_db_connection()
