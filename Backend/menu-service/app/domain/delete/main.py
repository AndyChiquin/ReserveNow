from flask import Flask
from app.config.settings import Config
from app.models.menu import db
from app.domain.delete.deleteMenu import delete_menu_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(delete_menu_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5303, debug=True)
