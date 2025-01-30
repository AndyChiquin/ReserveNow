from flask import Blueprint, jsonify
from app.database.database import get_connection

delete_bp = Blueprint("delete_restaurant", __name__)

@delete_bp.route("/restaurants/<int:restaurant_id>", methods=["DELETE"])
def delete_restaurant(restaurant_id):
    connection = get_connection()
    if connection is None:
        return jsonify({"error": "Unable to connect to the database"}), 500

    try:
        with connection.cursor() as cursor:
            # Instead of deleting, we update the status to “inactive”.
            cursor.execute("UPDATE restaurants SET status='inactive' WHERE id=%s", (restaurant_id,))
            connection.commit()

        return jsonify({"message": "Restaurant successfully deactivated"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()
