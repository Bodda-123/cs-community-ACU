import os
from flask import Flask

# 1) Define the Flask app directly in index.py to avoid ModuleNotFoundError
app = Flask(__name__)

# 2) Simple test route to confirm the server is running
@app.route("/")
def hello():
    return "Hello World - Flask is working on Render/Railway!"

# 3) Setup paths for future integration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.join(BASE_DIR, 'Sky_Hub_Project')

# Point static and template folders to your project directories
app.template_folder = os.path.join(PROJECT_DIR, 'templates')
app.static_folder = os.path.join(PROJECT_DIR, 'static')

if __name__ == "__main__":
    # Use the port defined by the environment (Render/Railway)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
