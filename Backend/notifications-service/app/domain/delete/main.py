from flask import Flask
from app.config.settings import db
from app.domain.delete.deleteNoti import delete_notification
from app.domain.delete.deleteNoti import delete_notification_bp

app = Flask(__name__)
app.config.from_object('app.config.settings.Config')

db.init_app(app)

app.register_blueprint(delete_notification_bp, url_prefix='/delete')

@app.route('/')
def hello_world():
    return 'Notifications Service is running!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5603, debug=True)
