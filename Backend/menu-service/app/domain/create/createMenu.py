import requests
from flask import Blueprint, request, jsonify
from app.models.menu import db, Menu  # ✅ SRP: Database model handling.

create_menu_bp = Blueprint('create_menu', __name__)

RESTAURANT_SERVICE_URL = "http://44.198.236.2:5002/restaurants"  # ✅ SRP: External service for restaurant validation.

def validate_request_data(data):
    """✅ SRP: Function responsible only for validating request data."""
    required_fields = ['restaurant_id', 'name', 'price']
    for field in required_fields:
        if field not in data:
            return f"Missing required field: {field}"
    return None

def check_restaurant_exists(restaurant_id):
    """✅ SRP: Function responsible only for checking if the restaurant exists."""
    response = requests.get(f"{RESTAURANT_SERVICE_URL}/{restaurant_id}")
    return response.status_code == 200

@create_menu_bp.route('/menu', methods=['POST'])
def create_menu():
    """✅ SRP: Function responsible only for handling the request and response."""
    data = request.get_json()

    validation_error = validate_request_data(data)  # ✅ SRP: Delegating validation.
    if validation_error:
        return jsonify({"message": validation_error}), 400

    if not check_restaurant_exists(data['restaurant_id']):  # ✅ SRP: Delegating restaurant validation.
        return jsonify({"message": "Restaurant not found"}), 404

    new_menu = Menu(
        restaurant_id=data['restaurant_id'],
        name=data['name'],
        price=data['price'],
        description=data.get('description', '')  # ✅ SRP: Default value handled here.
    )

    db.session.add(new_menu)
    db.session.commit()  # ✅ SRP: Database transaction handling.

    return jsonify({
        "message": "Menu item created successfully",
        "menu_id": new_menu.id
    }), 201  # ✅ SRP: Handling response separately.
