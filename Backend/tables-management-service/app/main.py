from fastapi import FastAPI
from app.domain.create.create import router as create_router
from app.domain.read.read import router as read_router
from app.domain.update.update import router as update_router
from app.domain.delete.delete import router as delete_router

app = FastAPI()

app.include_router(create_router)
app.include_router(read_router)
app.include_router(update_router)
app.include_router(delete_router)
