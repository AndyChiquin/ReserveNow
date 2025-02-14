from flask import Flask
from app.config.settings import db
from app.domain.create.createNoti import create_notification
from app.domain.create.createNoti import create_notification_bp

app = Flask(__name__)
app.config.from_object('app.config.settings.Config')

db.init_app(app)

app.register_blueprint(create_notification_bp, url_prefix='/create')

@app.route('/')
def hello_world():
    return 'Notifications Service is running!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5600, debug=True)
