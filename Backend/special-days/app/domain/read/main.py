from flask import Flask
from flask_migrate import Migrate
from app.config.settings import Config
from app.models.models import db
from app.domain.read.readSpecialDay import get_all_special_days, get_special_day_by_id

app = Flask(__name__)
app.config.from_object(Config)

# Inicializar base de datos y migraciones
db.init_app(app)
migrate = Migrate(app, db)

# Rutas del microservicio de lectura
app.add_url_rule("/read", "get_all_special_days", get_all_special_days, methods=["GET"])
app.add_url_rule("/read/<int:special_day_id>", "get_special_day_by_id", get_special_day_by_id, methods=["GET"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5401, debug=True)
