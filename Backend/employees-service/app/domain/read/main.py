from flask import Flask
from app.domain.read.read import read_bp

app = Flask(__name__)

# Register the Blueprint
app.register_blueprint(read_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5101, debug=True)
