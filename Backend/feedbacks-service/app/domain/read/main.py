from flask import Flask
from readFeedback import app  # ✅ YAGNI: Importing only the necessary module.

if __name__ == '__main__':
    # ✅ YAGNI: Running the app with only essential configurations.
    app.run(host='0.0.0.0', port=5201, debug=True)
