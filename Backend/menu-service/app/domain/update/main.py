from flask import Flask
from app.config.settings import Config
from app.models.menu import db
from app.domain.update.updateMenu import update_menu_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Registrar solo el Blueprint de "update"
app.register_blueprint(update_menu_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5302, debug=True)
