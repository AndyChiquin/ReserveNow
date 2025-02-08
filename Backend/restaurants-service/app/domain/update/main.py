from flask import Flask
from app.domain.update.update import update_bp

app = Flask(__name__)

# Register the blueprint for Update service
app.register_blueprint(update_bp)

if __name__ == "__main__":
    print("✅ Update Service is running on port 5003")
    app.run(host="0.0.0.0", port=5003, debug=True)
