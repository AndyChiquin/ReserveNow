from fastapi import APIRouter
from api.update.service import update_menu

router = APIRouter()

@router.put("/menus/{menu_id}")
def update_menu_endpoint(menu_id: int, name: str, description: str, status: str):
    return update_menu(menu_id, name, description, status)
