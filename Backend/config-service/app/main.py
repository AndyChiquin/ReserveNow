from fastapi import FastAPI
from app.db.config import Base, engine
from app.crud.create.route import router as create_router
from app.crud.read.route import router as read_router
from app.crud.delete.route import router as delete_router
from app.middleware import create_error_middleware

# Crear tablas automáticamente
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Config Service")

# Middleware para manejo global de errores
create_error_middleware(app)

# Registrar rutas
app.include_router(create_router)
app.include_router(read_router)
app.include_router(delete_router)

@app.get("/")
def root():
    return {"message": "Config Service is running"}
