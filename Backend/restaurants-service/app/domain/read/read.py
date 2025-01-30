from flask import Blueprint, jsonify
from app.database.database import get_connection

read_bp = Blueprint("read_restaurant", __name__)

# Get aLL restaurants
@read_bp.route("/restaurants", methods=["GET"])
def get_restaurants():
    connection = get_connection()
    if connection is None:
        return jsonify({"error": "Unable to connect to the database"}), 500

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM restaurants")
            results = cursor.fetchall()

        return jsonify(results), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()


# Get ONE restaurant by ID
@read_bp.route("/restaurants/<int:restaurant_id>", methods=["GET"])
def get_restaurant_by_id(restaurant_id):
    connection = get_connection()
    if connection is None:
        return jsonify({"error": "Unable to connect to the database"}), 500

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM restaurants WHERE id = %s", (restaurant_id,))
            restaurant = cursor.fetchone()

        if restaurant:
            return jsonify(restaurant), 200
        else:
            return jsonify({"message": "Restaurant not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()
