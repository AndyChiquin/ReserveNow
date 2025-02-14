from flask import Flask
from updateFeedback import app  # ✅ KISS: Importing only what is necessary.

if __name__ == '__main__':
    # ✅ KISS: Keeping the script simple and clear.
    app.run(host='0.0.0.0', port=5202, debug=True)
