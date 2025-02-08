from flask import Flask
from create import create_bp
from database.database import get_connection

app = Flask(__name__)

# Register the blueprint for Create service
app.register_blueprint(create_bp)

if __name__ == "__main__":
    print("✅ Create Service is running on port 5001")
    app.run(host="0.0.0.0", port=5001, debug=True)
