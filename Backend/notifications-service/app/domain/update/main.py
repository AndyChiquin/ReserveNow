from flask import Flask
from app.config.settings import db
from app.domain.update.updateNoti import update_notification
from app.domain.update.updateNoti import update_notification_bp

app = Flask(__name__)
app.config.from_object('app.config.settings.Config')

db.init_app(app)

app.register_blueprint(update_notification_bp, url_prefix='/update')

@app.route('/')
def hello_world():
    return 'Notifications Service is running!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5602, debug=True)
