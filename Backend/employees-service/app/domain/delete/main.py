from flask import Flask
from app.domain.delete.delete import delete_bp

app = Flask(__name__)

# Register the Blueprint
app.register_blueprint(delete_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5103, debug=True)
