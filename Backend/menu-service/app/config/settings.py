import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Cargar variables de entorno desde .env
load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}"
        f"@{os.getenv('DATABASE_HOST')}:{os.getenv('DATABASE_PORT')}/{os.getenv('DATABASE_NAME')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Probar la conexión a la base de datos
try:
    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
    with engine.connect() as conn:
        print("✅ Conexión exitosa a la base de datos en AWS RDS")
except Exception as e:
    print(f"❌ Error al conectar a la base de datos: {e}")
