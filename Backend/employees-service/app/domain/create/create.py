import json
import requests
from flask import Blueprint, request, jsonify
from app.database.database import get_redis_connection  # ✅ SRP: Handles only Redis connection.

create_bp = Blueprint("create_employee", __name__)
redis_client = get_redis_connection()  # ✅ SRP: Database connection responsibility.
VALID_ROLES = {"chef", "waiter", "manager", "cashier"}
RESTAURANT_SERVICE_URL = "http://44.198.236.2:5002/restaurants"  # ✅ SRP: External service URL definition.

def validar_restaurante(restaurant_id):
    """✅ SRP: Function responsible only for validating the restaurant existence."""
    try:
        response = requests.get(f"{RESTAURANT_SERVICE_URL}/{restaurant_id}", timeout=5)
        if response.status_code == 200:
            return True
        return False
    except requests.RequestException as e:
        print(f"Error connecting to Restaurant Service: {e}")
        return False

@create_bp.route("/employees", methods=["POST"])
def create_employee():
    """✅ SRP: Function responsible only for handling employee creation request."""
    data = request.json

    # ✅ SRP: Field validation is handled separately.
    required_fields = ["name", "role", "phone", "email", "salary", "restaurant_id"]
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        return jsonify({"error": f"The following required fields are missing: {', '.join(missing_fields)}"}), 400

    # ✅ SRP: Separate conditions for validating each field type.
    if not isinstance(data["name"], str) or not data["name"].strip():
        return jsonify({"error": "The name is mandatory and must be a valid text."}), 400

    if not isinstance(data["phone"], str) or not data["phone"].strip():
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

    # ✅ SRP: Restaurant validation is handled by a separate function.
    if not validar_restaurante(restaurant_id):
        return jsonify({"error": "The restaurant does not exist"}), 404

    # ✅ SRP: Generating a unique ID is separate from the employee creation logic.
    employee_id = redis_client.incr("employee_id")

    # ✅ SRP: Structuring employee data is handled independently.
    employee_data = {
        "id": employee_id,
        "name": data["name"].strip(),
        "role": data["role"],
        "phone": data["phone"].strip(),
        "email": data["email"].strip(),
        "salary": float(data["salary"]),
        "restaurant_id": restaurant_id
    }

    redis_client.set(f"employee:{employee_id}", json.dumps(employee_data))  # ✅ SRP: Storing in Redis.

    return jsonify({"message": "Employee successfully created", "employee": employee_data}), 201  # ✅ SRP: Handles response only.
