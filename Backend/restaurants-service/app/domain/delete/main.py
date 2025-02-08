from flask import Flask
from delete import delete_bp
from database.database import get_connection


app = Flask(__name__)

# Register the blueprint for Delete service
app.register_blueprint(delete_bp)

if __name__ == "__main__":
    print("✅ Delete Service is running on port 5004")
    app.run(host="0.0.0.0", port=5004, debug=True)
