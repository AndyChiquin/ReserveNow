import os
from dotenv import load_dotenv
import uvicorn
from fastapi import FastAPI
from src.routes.configReadRoutes import config_router

# Cargar variables de entorno
load_dotenv()

app = FastAPI(title="Config Service - Read")

app.include_router(config_router)

@app.get("/")
def root():
    return {"message": "Config Service READ is running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8002)))
