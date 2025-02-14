from flask import Blueprint, jsonify
from app.models.menu import db, Menu

read_menu_bp = Blueprint('read_menu', __name__)

@read_menu_bp.route('/menu/<int:menu_id>', methods=['GET'])
def read_menu(menu_id):
    """ Busca un menú por su ID """
    menu_item = db.session.get(Menu, menu_id)  
    
    if not menu_item:
        return jsonify({"message": "Menu item not found"}), 404

    return jsonify({
        "id": menu_item.id,
        "restaurant_id": menu_item.restaurant_id,
        "name": menu_item.name,
        "price": float(menu_item.price),  
        "description": menu_item.description
    })

@read_menu_bp.route('/menu', methods=['GET'])
def get_all_menus():
    """ Obtiene todos los menús de la base de datos """
    menus = Menu.query.all()

    if not menus:
        return jsonify({"message": "No menus found"}), 404

    return jsonify([
        {
            "id": menu.id,
            "restaurant_id": menu.restaurant_id,
            "name": menu.name,
            "price": float(menu.price),  
            "description": menu.description
        } for menu in menus
    ])
