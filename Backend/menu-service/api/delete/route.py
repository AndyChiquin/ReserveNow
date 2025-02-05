from fastapi import APIRouter
from api.delete.service import delete_menu

router = APIRouter()

@router.delete("/menus/{menu_id}")
def delete_menu_endpoint(menu_id: int):
    return delete_menu(menu_id)
