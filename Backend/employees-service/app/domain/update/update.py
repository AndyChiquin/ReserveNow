import json
import requests
from flask import Blueprint, request, jsonify
from app.database.database import get_redis_connection

update_bp = Blueprint("update_employee", __name__)
redis_client = get_redis_connection()

RESTAURANT_SERVICE_URL = "http://44.198.236.2:5002/restaurants"

def validar_restaurante(restaurant_id):
    """Check if the restaurant exists in the restaurant service."""
    try:
        response = requests.get(f"{RESTAURANT_SERVICE_URL}/{restaurant_id}", timeout=5)
        if response.status_code == 200:
            return True
        return False
    except requests.RequestException as e:
        print(f"Error connecting to Restaurant Service: {e}")
        return False

@update_bp.route("/employees/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):
    """Update employee data (can be salary, role, phone number, etc.)"""
    data = request.json

    # Get current employee data
    employee_data = redis_client.get(f"employee:{employee_id}")

    if not employee_data:
        print(f"Employee with ID {employee_id} not found")  
        return jsonify({"error": "Employee not found"}), 404

    employee = json.loads(employee_data)

    # If the restaurant is changed, validate first
    if "restaurant_id" in data:
        new_restaurant_id = data["restaurant_id"]
        print(f"Trying to switch to restaurant ID: {new_restaurant_id}")

        if not isinstance(new_restaurant_id, int) or new_restaurant_id <= 0:
            return jsonify({"error": "The restaurant_id must be a positive integer."}), 400

        if not validar_restaurante(new_restaurant_id):
            print("Invalid restaurant, update cancelled")
            return jsonify({"error": "The restaurant does not exist"}), 404

        employee["restaurant_id"] = new_restaurant_id

    # Update other fields if they exist and are valid
    allowed_fields = {"name", "role", "phone", "email", "salary"}
    for key, value in data.items():
        if key in allowed_fields:
            employee[key] = value

    redis_client.set(f"employee:{employee_id}", json.dumps(employee))

    print(f"Employee {employee_id} updated successfully")  
    return jsonify({"message": "Employee successfully updated", "employee": employee}), 200
