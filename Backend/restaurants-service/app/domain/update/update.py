from flask import Blueprint, request, jsonify
from app.database.database import get_connection  # ✅ OCP: Database connection is abstracted.

update_bp = Blueprint("update_restaurant", __name__)

def validate_status(new_status):
    """✅ OCP: Function responsible only for validating status."""
    if new_status not in ["active", "inactive"]:
        return "Invalid status. Must be 'active' or 'inactive'"
    return None  # No error

def update_status_in_db(restaurant_id, new_status):
    """✅ OCP: Function responsible only for updating restaurant status in the database."""
    connection = get_connection()
    if connection is None:
        return {"error": "Unable to connect to the database"}, 500

    try:
        with connection.cursor() as cursor:
            cursor.execute("UPDATE restaurants SET status=%s WHERE id=%s", (new_status, restaurant_id))
            connection.commit()
        return {"message": "Restaurant status successfully updated"}, 200
    except Exception as e:
        return {"error": str(e)}, 500
    finally:
        connection.close()  # ✅ OCP: Database connection logic remains unchanged.

@update_bp.route("/restaurants/<int:restaurant_id>/status", methods=["PUT"])
def update_restaurant_status(restaurant_id):
    """✅ OCP: Main function now delegates logic to helper functions."""
    data = request.json
    new_status = data.get("status")

    # ✅ OCP: Status validation logic is externalized for extensibility.
    validation_error = validate_status(new_status)
    if validation_error:
        return jsonify({"error": validation_error}), 400

    # ✅ OCP: Delegating database update logic.
    response, status = update_status_in_db(restaurant_id, new_status)
    return jsonify(response), status
