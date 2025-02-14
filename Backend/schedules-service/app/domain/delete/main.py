from flask import Flask
from app.domain.delete.deleteSchedule import delete_bp

app = Flask(__name__)

app.register_blueprint(delete_bp)

if __name__ == "__main__":
    print("Delete Service is running on port 5500")
    app.run(host="0.0.0.0", port=5500, debug=True)
