from flask import Blueprint, request, jsonify
from app.database.database import get_connection

create_bp = Blueprint("create_restaurant", __name__)

@create_bp.route("/restaurants", methods=["POST"])
def create_restaurant():
    data = request.json
    connection = get_connection()
    if connection is None:
        return jsonify({"error": "Unable to connect to the database"}), 500

    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO restaurants (name, address, phone, email, status)
                VALUES (%s, %s, %s, %s, %s)
            """, (data["name"], data["address"], data["phone"], data["email"], data.get("status", "active")))
            connection.commit()

        return jsonify({"message": "Successfully created restaurant"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        connection.close()
