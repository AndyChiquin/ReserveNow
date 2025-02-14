from flask import Blueprint, jsonify
from app.database.database import get_redis_connection  # ✅ DRY: Reusing Redis connection setup.
import json

read_bp = Blueprint("read_employee", __name__)
redis_client = get_redis_connection()  # ✅ DRY: Single instance of Redis client.

def fetch_employee(employee_id):
    """✅ DRY: Centralized function to fetch an employee by ID from Redis."""
    employee_data = redis_client.get(f"employee:{employee_id}")
    return json.loads(employee_data) if employee_data else None

@read_bp.route("/employees", methods=["GET"])
def get_employees():
    """✅ DRY: Fetch all employees from Redis."""
    employee_keys = redis_client.keys("employee:*")
    employees = [json.loads(redis_client.get(key)) for key in employee_keys]  # ✅ DRY: Using a list comprehension.

    return jsonify(employees), 200

@read_bp.route("/employees/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):
    """✅ DRY: Get an employee by ID using a helper function."""
    employee = fetch_employee(employee_id)  # ✅ DRY: Using reusable function.

    if not employee:
        return jsonify({"error": "Employee not found"}), 404

    return jsonify(employee), 200
