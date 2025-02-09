from flask import Flask
from deleteFeedback import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5203, debug=True)
