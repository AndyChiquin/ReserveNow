from flask import Blueprint, jsonify
from app.database.database import get_redis_connection  # ✅ KISS: Simple, clear database connection.

delete_bp = Blueprint("delete_employee", __name__)
redis_client = get_redis_connection()  # ✅ KISS: Reusing Redis connection without complexity.

@delete_bp.route("/employees/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    """✅ KISS: Simple function to delete an employee from Redis."""
    employee_key = f"employee:{employee_id}"  # ✅ KISS: Clear, straightforward key generation.

    if redis_client.exists(employee_key):  # ✅ KISS: Direct check if the employee exists.
        redis_client.delete(employee_key)  # ✅ KISS: Direct deletion without unnecessary operations.
        print(f"Employee {employee_id} successfully deleted")  # Debug log
        return jsonify({"message": "Employee successfully removed"}), 200

    print(f"Employee {employee_id} not found")  # Debug log
    return jsonify({"error": "Employee not found"}), 404  # ✅ KISS: Simple, clear error handling.
