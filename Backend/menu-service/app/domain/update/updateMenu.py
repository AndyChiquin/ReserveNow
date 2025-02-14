import requests
from flask import Blueprint, request, jsonify
from app.models.menu import db, Menu

update_menu_bp = Blueprint('update_menu', __name__)

RESTAURANT_SERVICE_URL = "http://44.198.236.2:5002/restaurants"

@update_menu_bp.route('/menu/<int:menu_id>', methods=['PUT'])
def update_menu(menu_id):
    data = request.get_json()
    menu_item = Menu.query.get(menu_id)

    if not menu_item:
        return jsonify({"message": "Menu item not found"}), 404

    if not any(key in data for key in ['restaurant_id', 'name', 'price']):
        return jsonify({"message": "At least one of restaurant_id, name, or price must be provided"}), 400

    if 'restaurant_id' in data:
        response = requests.get(f"{RESTAURANT_SERVICE_URL}/{data['restaurant_id']}")
        if response.status_code != 200:
            return jsonify({"message": "Invalid restaurant_id. Restaurant not found"}), 404
        menu_item.restaurant_id = data['restaurant_id']

    menu_item.name = data.get('name', menu_item.name)
    menu_item.price = data.get('price', menu_item.price)
    menu_item.description = data.get('description', menu_item.description)

    db.session.commit()

    return jsonify({"message": "Menu item updated successfully"})
