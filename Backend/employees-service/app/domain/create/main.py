from flask import Flask
from app.domain.create.create import create_bp

app = Flask(__name__)

# Register the Blueprint
app.register_blueprint(create_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5100, debug=True)
