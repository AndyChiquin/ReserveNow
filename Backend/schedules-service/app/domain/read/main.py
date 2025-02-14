from flask import Flask
from app.domain.read.readSchedule import read_bp

app = Flask(__name__)

app.register_blueprint(read_bp)

if __name__ == "__main__":
    print("Read Service is running on port 5500")
    app.run(host="0.0.0.0", port=5500, debug=True)
