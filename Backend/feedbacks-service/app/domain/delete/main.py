from flask import Flask
from deleteFeedback import app  # ✅ KISS: Importing only what is necessary.

if __name__ == '__main__':
    # ✅ KISS: Simple and clear execution without unnecessary complexity.
    app.run(host='0.0.0.0', port=5203, debug=True)
