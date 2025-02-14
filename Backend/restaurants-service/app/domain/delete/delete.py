from flask import Blueprint, jsonify
from app.database.database import get_connection  # ✅ KISS: Simple database connection import.

delete_bp = Blueprint("delete_restaurant", __name__)

@delete_bp.route("/restaurants/<int:restaurant_id>", methods=["DELETE"])
def delete_restaurant(restaurant_id):
    """✅ KISS: Simple function to deactivate a restaurant by updating its status."""
    connection = get_connection()
    
    if connection is None:
        return jsonify({"error": "Unable to connect to the database"}), 500  # ✅ KISS: Clear and concise error handling.

    try:
        with connection.cursor() as cursor:
            # ✅ KISS: Instead of physically deleting, we simply mark the restaurant as inactive.
            cursor.execute("UPDATE restaurants SET status='inactive' WHERE id=%s", (restaurant_id,))
            connection.commit()  # ✅ KISS: Direct commit to finalize the update.

        return jsonify({"message": "Restaurant successfully deactivated"}), 200  # ✅ KISS: Clear success message.
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # ✅ KISS: Simple error response.
    finally:
        connection.close()  # ✅ KISS: Always close the database connection.
