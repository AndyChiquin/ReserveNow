from flask import Flask
from app.domain.create.create import create_bp
from app.domain.read.read import read_bp
from app.domain.update.update import update_bp
from app.domain.delete.delete import delete_bp

app = Flask(__name__)

app.register_blueprint(create_bp)
app.register_blueprint(read_bp)
app.register_blueprint(update_bp)
app.register_blueprint(delete_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
