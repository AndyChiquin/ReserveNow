from flask import Blueprint, jsonify
from app.database.database import get_redis_connection

delete_bp = Blueprint("delete_employee", __name__)
redis_client = get_redis_connection()

@delete_bp.route("/employees/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    """Delete a Redis employee by ID”."""
    if redis_client.exists(f"employee:{employee_id}"):
        redis_client.delete(f"employee:{employee_id}")
        return jsonify({"message": "Employee successfully removed"}), 200
    return jsonify({"error": "Employee not found"}), 404
