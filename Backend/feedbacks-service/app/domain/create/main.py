from flask import Flask
from createFeedback import app  # ✅ YAGNI: Only importing what is necessary.

if __name__ == '__main__':
    # ✅ YAGNI: Running the app with minimal configuration.
    app.run(host='0.0.0.0', port=5200, debug=True)
