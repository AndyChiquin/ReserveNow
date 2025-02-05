from fastapi import APIRouter
from api.read.service import get_menus

router = APIRouter()

@router.get("/menus/")
def get_menus_endpoint():
    return get_menus()
