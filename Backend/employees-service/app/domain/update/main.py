from flask import Flask
from app.domain.update.update import update_bp

app = Flask(__name__)

# Register the Blueprint
app.register_blueprint(update_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5102, debug=True)
