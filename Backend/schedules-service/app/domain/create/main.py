from flask import Flask
from app.domain.create.createSchedule import create_bp

app = Flask(__name__)

app.register_blueprint(create_bp)

if __name__ == "__main__":
    print("Create Service is running on port 5500")
    app.run(host="0.0.0.0", port=5500, debug=True)
