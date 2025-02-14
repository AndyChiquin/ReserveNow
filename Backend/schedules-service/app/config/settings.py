import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Cargar variables de entorno
load_dotenv()

# Configurar Flask
app = Flask(__name__)

# Obtener valores del entorno
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

# Configurar la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializar SQLAlchemy
db = SQLAlchemy(app)

# Probar conexión
try:
    with app.app_context():
        db.engine.connect()
        print(" Conexión establecida correctamente a la base de datos.")
except Exception as e:
    print(f"Error al conectar con la base de datos: {e}")
