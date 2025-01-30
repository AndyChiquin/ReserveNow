from flask import Blueprint, request, jsonify
from app.database.database import get_connection

update_bp = Blueprint("update_restaurant", __name__)

# Modify ONLY the status of a restaurant
@update_bp.route("/restaurants/<int:restaurant_id>/status", methods=["PUT"])
def update_restaurant_status(restaurant_id):
    data = request.json
    new_status = data.get("status")

    if new_status not in ["active", "inactive"]:
        return jsonify({"error": "Invalid status. Must be 'active' or 'inactive'"}), 400

    connection = get_connection()
    if connection is None:
        return jsonify({"error": "Unable to connect to the database"}), 500

    try:
        with connection.cursor() as cursor:
            cursor.execute("UPDATE restaurants SET status=%s WHERE id=%s", (new_status, restaurant_id))
            connection.commit()

        return jsonify({"message": "Restaurant status successfully updated"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()
