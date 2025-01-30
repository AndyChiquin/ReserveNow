from flask import Blueprint, request, jsonify
from app.database.database import get_redis_connection
from app.utils.restaurant_service import validar_restaurante
import json

create_bp = Blueprint("create_employee", __name__)
redis_client = get_redis_connection()
VALID_ROLES = {"chef", "waiter", "manager", "cashier"}

@create_bp.route("/employees", methods=["POST"])
def create_employee():
    """Create an employee in Redis validating the data and the restaurant"""
    data = request.json

    # Validate that all required fields are present
    required_fields = ["name", "role", "phone", "email", "salary", "restaurant_id"]
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        return jsonify({"error": f"The following required fields are missing: {', '.join(missing_fields)}"}), 400

    # Individual validations
    if not isinstance(data["name"], str) or len(data["name"].strip()) == 0:
        return jsonify({"error": "The name is mandatory and must be a valid text."}), 400

    if not isinstance(data["phone"], str) or len(data["phone"].strip()) == 0:
        return jsonify({"error": "The phone number is mandatory and must be a valid text."}), 400

    if not isinstance(data["email"], str) or "@" not in data["email"]:
        return jsonify({"error": "The email must be valid"}), 400

    if not isinstance(data["salary"], (int, float)) or data["salary"] < 0:
        return jsonify({"error": "Salary must be a positive number"}), 400

    if data["role"] not in VALID_ROLES:
        return jsonify({"error": f"Invalid role. Must be one of: {', '.join(VALID_ROLES)}"}), 400

    restaurant_id = data["restaurant_id"]
    if not isinstance(restaurant_id, int) or restaurant_id <= 0:
        return jsonify({"error": "The restaurant_id must be a positive integer number."}), 400

    # 🔹 Check if the restaurant exists before assigning it.
    if not validar_restaurante(restaurant_id):
        return jsonify({"error": "The restaurant does not exist"}), 404

    # Generate unique ID
    employee_id = redis_client.incr("employee_id")

    # Create employee structure
    employee_data = {
        "id": employee_id,
        "name": data["name"].strip(),
        "role": data["role"],
        "phone": data["phone"].strip(),
        "email": data["email"].strip(),
        "salary": float(data["salary"]),
        "restaurant_id": restaurant_id
    }

    redis_client.set(f"employee:{employee_id}", json.dumps(employee_data))

    return jsonify({"message": "Employee successfully created", "employee": employee_data}), 201
