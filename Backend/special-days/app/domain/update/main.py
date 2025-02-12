from flask import Flask
from flask_migrate import Migrate
from app.config.settings import Config
from app.models.models import db
from app.domain.update.updateSpecialDay import update_special_day

app = Flask(__name__)
app.config.from_object(Config)

# Inicializar base de datos y migraciones
db.init_app(app)
migrate = Migrate(app, db)

# Ruta para actualizar un día especial
app.add_url_rule("/update/<int:special_day_id>", "update_special_day", update_special_day, methods=["PUT"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5402, debug=True)
