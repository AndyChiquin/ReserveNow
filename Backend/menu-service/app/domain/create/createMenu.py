import requests
from flask import Blueprint, request, jsonify
from app.models.menu import db, Menu

create_menu_bp = Blueprint('create_menu', __name__)

RESTAURANT_SERVICE_URL = "http://44.198.236.2:5002/restaurants" 

@create_menu_bp.route('/menu', methods=['POST'])
def create_menu():
    data = request.get_json()

    required_fields = ['restaurant_id', 'name', 'price']
    for field in required_fields:
        if field not in data:
            return jsonify({"message": f"Missing required field: {field}"}), 400

    restaurant_id = data['restaurant_id']

    response = requests.get(f"{RESTAURANT_SERVICE_URL}/{restaurant_id}")

    if response.status_code != 200:
        return jsonify({"message": "Restaurant not found"}), 404

    new_menu = Menu(
        restaurant_id=restaurant_id,
        name=data['name'],
        price=data['price'],
        description=data.get('description', '')
    )

    db.session.add(new_menu)
    db.session.commit()

    return jsonify({
        "message": "Menu item created successfully",
        "menu_id": new_menu.id
    }), 201
