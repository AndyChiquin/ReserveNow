from flask import Flask
from app.config.settings import Config
from app.models.menu import db
from app.domain.read.readMenu import read_menu_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Registrar solo el Blueprint de "read"
app.register_blueprint(read_menu_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5301, debug=True)
