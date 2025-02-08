from fastapi import APIRouter
from src.Controller.configReadController import router

config_router = APIRouter()
config_router.include_router(router, prefix="/api")
