import requests
from flask import Blueprint, request, jsonify
from app.models.menu import db, Menu  # ✅ OCP: Database interaction is abstracted through SQLAlchemy.

update_menu_bp = Blueprint('update_menu', __name__)

RESTAURANT_SERVICE_URL = "http://44.198.236.2:5002/restaurants"  # ✅ OCP: External service dependency.

def validate_restaurant(restaurant_id):
    """✅ OCP: Function responsible only for validating if the restaurant exists."""
    response = requests.get(f"{RESTAURANT_SERVICE_URL}/{restaurant_id}")
    return response.status_code == 200

def update_menu_fields(menu_item, data):
    """✅ OCP: Function responsible for updating menu attributes."""
    if 'restaurant_id' in data:
        if not validate_restaurant(data['restaurant_id']):
            return "Invalid restaurant_id. Restaurant not found"
        menu_item.restaurant_id = data['restaurant_id']

    menu_item.name = data.get('name', menu_item.name)
    menu_item.price = data.get('price', menu_item.price)
    menu_item.description = data.get('description', menu_item.description)

    return None  # No error

@update_menu_bp.route('/menu/<int:menu_id>', methods=['PUT'])
def update_menu(menu_id):
    """✅ OCP: The main function now only controls the flow."""
    data = request.get_json()
    menu_item = Menu.query.get(menu_id)

    if not menu_item:
        return jsonify({"message": "Menu item not found"}), 404

    if not any(key in data for key in ['restaurant_id', 'name', 'price']):
        return jsonify({"message": "At least one of restaurant_id, name, or price must be provided"}), 400

    error = update_menu_fields(menu_item, data)  # ✅ OCP: Delegating field updates.
    if error:
        return jsonify({"message": error}), 404

    db.session.commit()  # ✅ OCP: The commit logic remains unchanged.

    return jsonify({"message": "Menu item updated successfully"})
