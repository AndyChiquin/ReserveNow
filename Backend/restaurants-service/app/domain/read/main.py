from flask import Flask
from app.domain.read.read import read_bp

app = Flask(__name__)

# Register the blueprint for Read service
app.register_blueprint(read_bp)

if __name__ == "__main__":
    print("✅ Read Service is running on port 5002")
    app.run(host="0.0.0.0", port=5002, debug=True)
