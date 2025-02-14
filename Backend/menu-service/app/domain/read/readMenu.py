from flask import Blueprint, jsonify
from app.models.menu import db, Menu  # ✅ DRY: Importing database and model once.

read_menu_bp = Blueprint('read_menu', __name__)

def serialize_menu(menu):
    """✅ DRY: Centralized function to convert a menu item to a dictionary."""
    return {
        "id": menu.id,
        "restaurant_id": menu.restaurant_id,
        "name": menu.name,
        "price": float(menu.price),  # ✅ DRY: Handling type conversion in one place.
        "description": menu.description
    }

@read_menu_bp.route('/menu/<int:menu_id>', methods=['GET'])
def read_menu(menu_id):
    """✅ DRY: Fetches a single menu item by ID."""
    menu_item = db.session.get(Menu, menu_id)  
    
    if not menu_item:
        return jsonify({"message": "Menu item not found"}), 404

    return jsonify(serialize_menu(menu_item))  # ✅ DRY: Reusing serialization function.

@read_menu_bp.route('/menu', methods=['GET'])
def get_all_menus():
    """✅ DRY: Fetches all menu items from the database."""
    menus = Menu.query.all()

    if not menus:
        return jsonify({"message": "No menus found"}), 404

    return jsonify([serialize_menu(menu) for menu in menus])  # ✅ DRY: Reusing serialization function.
