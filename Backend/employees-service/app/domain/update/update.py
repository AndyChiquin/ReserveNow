from flask import Blueprint, request, jsonify
from app.database.database import get_redis_connection
from app.utils.restaurant_service import validar_restaurante
import json

update_bp = Blueprint("update_employee", __name__)
redis_client = get_redis_connection()

@update_bp.route("/employees/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):
    """Maintain employee data (can be salary, role, phone number, etc.)"""
    data = request.json

    # Obtain current employee data
    employee_data = redis_client.get(f"employee:{employee_id}")

    if not employee_data:
        print(f"Employee with ID {employee_id} not found")  
        return jsonify({"error": "Employee not found"}), 404

    employee = json.loads(employee_data)

    # If you try to change the restaurant, first validate
    if "restaurant_id" in data:
        new_restaurant_id = data["restaurant_id"]
        print(f"Trying to switch to restaurant ID: {new_restaurant_id}")

        if not validar_restaurante(new_restaurant_id):
            print("Invalid restaurant, update cancelled")  # <-- Debug
            return jsonify({"error": "The restaurant does not exist"}), 404

        employee["restaurant_id"] = new_restaurant_id

    # Update other fields if they exist
    for key, value in data.items():
        if key in employee and key != "restaurant_id":
            employee[key] = value

    redis_client.set(f"employee:{employee_id}", json.dumps(employee))

    print(f"Employee {employee_id} apdated")  # <-- Debug
    return jsonify({"message": "Employee successfully updated", "employee": employee}), 200
