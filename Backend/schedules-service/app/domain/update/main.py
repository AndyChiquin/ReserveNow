from flask import Flask
from app.domain.update.updateSchedule import update_bp

app = Flask(__name__)

app.register_blueprint(update_bp)

if __name__ == "__main__":
    print("Update Service is running on port 5500")
    app.run(host="0.0.0.0", port=5500, debug=True)
