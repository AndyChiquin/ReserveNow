import sys
import os
from flask import Flask, jsonify

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from database.database import get_connection

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    """Ruta raíz para verificar que el microservicio está activo"""
    return jsonify({"message": "Microservicio de lectura de feedbacks activo"}), 200

@app.route('/feedbacks', methods=['GET'])
def get_feedbacks():
    """Obtiene todos los feedbacks de la base de datos"""
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, user_id, restaurant_id, rating, comment, created_at FROM feedbacks")
            rows = cursor.fetchall()
            feedbacks = [dict(zip([column[0] for column in cursor.description], row)) for row in rows]
            cursor.close()
            conn.close()
            return jsonify(feedbacks), 200
        except Exception as e:
            return jsonify({"error": f"Error al obtener feedbacks: {str(e)}"}), 500

    return jsonify({"error": "Error en la conexión a la base de datos"}), 500

@app.route('/feedbacks/<int:feedback_id>', methods=['GET'])
def get_feedback_by_id(feedback_id):
    """Obtiene un feedback específico por ID"""
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, user_id, restaurant_id, rating, comment, created_at FROM feedbacks WHERE id = ?", (feedback_id,))
            row = cursor.fetchone()
            cursor.close()
            conn.close()
            if row:
                feedback = dict(zip(["id", "user_id", "restaurant_id", "rating", "comment", "created_at"], row))
                return jsonify(feedback), 200
            else:
                return jsonify({"error": "Feedback no encontrado"}), 404
        except Exception as e:
            return jsonify({"error": f"Error al obtener feedback: {str(e)}"}), 500

    return jsonify({"error": "Error en la conexión a la base de datos"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5201, debug=True)
