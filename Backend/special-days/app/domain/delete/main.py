from flask import Flask
from flask_migrate import Migrate
from app.config.settings import Config
from app.models.models import db
from app.domain.delete.deleteSpecialDay import delete_special_day

app = Flask(__name__)
app.config.from_object(Config)

# Inicializar base de datos y migraciones
db.init_app(app)
migrate = Migrate(app, db)

# Ruta para eliminar un día especial
app.add_url_rule("/delete/<int:special_day_id>", "delete_special_day", delete_special_day, methods=["DELETE"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5403, debug=True)
