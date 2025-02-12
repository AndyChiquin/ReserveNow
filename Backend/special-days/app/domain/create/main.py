from flask import Flask
from flask_migrate import Migrate
from app.config.settings import Config
from app.models.models import db
from app.domain.create.createSpecialDay import create_special_day

app = Flask(__name__)
app.config.from_object(Config)

# Inicializar base de datos y migraciones
db.init_app(app)
migrate = Migrate(app, db)

# Rutas del microservicio
app.add_url_rule("/create", "create_special_day", create_special_day, methods=["POST"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5400, debug=True)
