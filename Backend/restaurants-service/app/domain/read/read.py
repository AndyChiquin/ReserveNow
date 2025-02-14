from flask import Blueprint, jsonify
from app.database.database import get_connection  # ✅ DRY: Reusing database connection.

read_bp = Blueprint("read_restaurant", __name__)

def fetch_data(query, params=None):
    """✅ DRY: Function to execute a database query and return results."""
    connection = get_connection()
    if connection is None:
        return {"error": "Unable to connect to the database"}, 500

    try:
        with connection.cursor() as cursor:
            cursor.execute(query, params or ())
            results = cursor.fetchall()
        return results, 200
    except Exception as e:
        return {"error": str(e)}, 500
    finally:
        connection.close()

# ✅ DRY: Function for fetching all restaurants.
@read_bp.route("/restaurants", methods=["GET"])
def get_restaurants():
    results, status = fetch_data("SELECT * FROM restaurants")
    return jsonify(results), status

# ✅ DRY: Function for fetching a restaurant by ID.
@read_bp.route("/restaurants/<int:restaurant_id>", methods=["GET"])
def get_restaurant_by_id(restaurant_id):
    results, status = fetch_data("SELECT * FROM restaurants WHERE id = %s", (restaurant_id,))
    
    if status == 200 and results:
        return jsonify(results[0]), 200  # ✅ DRY: Fetching the first row directly.
    
    return jsonify({"message": "Restaurant not found"}), 404
