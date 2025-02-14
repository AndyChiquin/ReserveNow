import sys
import os
from flask import Flask, request, jsonify

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from database.database import get_connection
from utils.validators import user_exists, reservation_exists, restaurant_exists

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    """Ruta raíz para verificar que el microservicio está activo"""
    return jsonify({"message": "Microservicio de Feedbacks activo"}), 200

@app.route('/feedbacks', methods=['POST'])
def create_feedback():
    """Crea un nuevo feedback después de validar usuario, reserva y restaurante"""
    data = request.json
    user_id = data.get('user_id')
    reservation_id = data.get('reservation_id')
    restaurant_id = data.get('restaurant_id')

    if not user_id or not reservation_id or not restaurant_id:
        return jsonify({"error": "user_id, reservation_id y restaurant_id son obligatorios"}), 400

    if not user_exists(user_id):
        return jsonify({"error": "El usuario no existe"}), 400

    if not reservation_exists(reservation_id):
        return jsonify({"error": "La reserva no existe"}), 400

    if not restaurant_exists(restaurant_id):
        return jsonify({"error": "El restaurante no existe"}), 400

    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO feedbacks (user_id, restaurant_id, rating, comment)
                VALUES (?, ?, ?, ?)
            """, (user_id, restaurant_id, data['rating'], data.get('comment', '')))
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify({"message": "Feedback creado exitosamente"}), 201
        except Exception as e:
            return jsonify({"error": f"Error al insertar feedback: {str(e)}"}), 500

    return jsonify({"error": "Error de conexión con la base de datos"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5200, debug=True)
