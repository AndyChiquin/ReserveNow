from flask import Blueprint, jsonify
from app.database.database import get_redis_connection
import json

read_bp = Blueprint("read_employee", __name__)

redis_client = get_redis_connection()

@read_bp.route("/employees", methods=["GET"])
def get_employees():
    employee_keys = redis_client.keys("employee:*")
    employees = [json.loads(redis_client.get(key)) for key in employee_keys]

    return jsonify(employees), 200

@read_bp.route("/employees/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):
    """Get an employee by ID from Redis"""
    employee_data = redis_client.get(f"employee:{employee_id}")
    
    if not employee_data:
        return jsonify({"error": "Employee not found"}), 404

    return jsonify(json.loads(employee_data)), 200
