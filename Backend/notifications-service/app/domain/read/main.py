from flask import Flask
from app.config.settings import db
from app.domain.read.readNoti import get_notifications_by_user
from app.domain.read.readNoti import read_notification_bp

app = Flask(__name__)
app.config.from_object('app.config.settings.Config')

db.init_app(app)

app.register_blueprint(read_notification_bp, url_prefix='/read')

@app.route('/')
def hello_world():
    return 'Notifications Service is running!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5601, debug=True)
