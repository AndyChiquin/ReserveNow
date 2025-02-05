from fastapi import APIRouter
from api.create.service import create_menu

router = APIRouter()

@router.post("/menus/")
def create_menu_endpoint(name: str, description: str, status: str):
    return create_menu(name, description, status)
