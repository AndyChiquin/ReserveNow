from fastapi import FastAPI
from app.routes import router
from app.config import Base, engine

# Crear las tablas automáticamente si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Config Service")
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Config Service is running"}
