from flask import Blueprint, jsonify
from app.database.database import get_redis_connection

delete_bp = Blueprint("delete_employee", __name__)
redis_client = get_redis_connection()

@delete_bp.route("/employees/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    """Delete an employee from Redis by ID."""
    employee_key = f"employee:{employee_id}"

    if redis_client.exists(employee_key):
        redis_client.delete(employee_key)
        print(f"Employee {employee_id} successfully deleted")  # Debug log
        return jsonify({"message": "Employee successfully removed"}), 200

    print(f"Employee {employee_id} not found")  # Debug log
    return jsonify({"error": "Employee not found"}), 404
