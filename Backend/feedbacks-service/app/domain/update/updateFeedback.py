import sys
import os
from flask import Flask, request, jsonify

# Agregar la raíz del proyecto al path para evitar errores de importación
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from database.database import get_connection
from utils.validators import user_exists, reservation_exists, restaurant_exists

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    """Ruta raíz para verificar que el microservicio está activo"""
    return jsonify({"message": "Microservicio de actualización de feedbacks activo"}), 200

@app.route('/feedbacks/<int:feedback_id>', methods=['PUT'])
def update_feedback(feedback_id):
    """Actualiza un feedback en la base de datos"""
    data = request.json
    user_id = data.get('user_id')
    reservation_id = data.get('reservation_id')
    restaurant_id = data.get('restaurant_id')

    if not user_id or not reservation_id or not restaurant_id:
        return jsonify({"error": "user_id, reservation_id y restaurant_id son obligatorios"}), 400

    # Validar usuario
    if not user_exists(user_id):
        return jsonify({"error": "El usuario no existe"}), 400

    # Validar reserva
    if not reservation_exists(reservation_id):
        return jsonify({"error": "La reserva no existe"}), 400

    # Validar restaurante
    if not restaurant_exists(restaurant_id):
        return jsonify({"error": "El restaurante no existe"}), 400

    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM feedbacks WHERE id = ?", (feedback_id,))
            existing_feedback = cursor.fetchone()

            if not existing_feedback:
                return jsonify({"error": "Feedback no encontrado"}), 404

            cursor.execute("""
                UPDATE feedbacks 
                SET user_id = ?, restaurant_id = ?, rating = ?, comment = ?
                WHERE id = ?
            """, (user_id, restaurant_id, data['rating'], data.get('comment', ''), feedback_id))
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify({"message": "Feedback actualizado correctamente"}), 200
        except Exception as e:
            return jsonify({"error": f"Error al actualizar feedback: {str(e)}"}), 500

    return jsonify({"error": "Error en la conexión a la base de datos"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5202, debug=True)
