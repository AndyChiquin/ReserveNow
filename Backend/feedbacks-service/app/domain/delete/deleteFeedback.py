import sys
import os
from flask import Flask, jsonify

# ✅ DIP: Adjusting the system path to dynamically locate modules.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from database.database import get_connection  # ✅ DIP: The database connection is abstracted.

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    """✅ DIP: High-level module (Flask route) does not depend on low-level database logic."""
    return jsonify({"message": "Microservicio de eliminación de feedbacks activo"}), 200

@app.route('/feedbacks/<int:feedback_id>', methods=['DELETE'])
def delete_feedback(feedback_id):
    """✅ DIP: This function depends on an abstraction (get_connection) instead of a concrete database implementation."""
    conn = get_connection()  # ✅ DIP: Abstracted database connection.

    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM feedbacks WHERE id = ?", (feedback_id,))
            existing_feedback = cursor.fetchone()

            if not existing_feedback:
                return jsonify({"error": "Feedback no encontrado"}), 404

            cursor.execute("DELETE FROM feedbacks WHERE id = ?", (feedback_id,))
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify({"message": "Feedback eliminado correctamente"}), 200
        except Exception as e:
            return jsonify({"error": f"Error al eliminar feedback: {str(e)}"}), 500

    return jsonify({"error": "Error en la conexión a la base de datos"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5203, debug=True)  # ✅ DIP: The app configuration is externalized.
