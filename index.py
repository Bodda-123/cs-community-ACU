import os
import sys
from flask import Flask

# 1) Define the Flask app directly inside index.py
app = Flask(__name__)

# 2) Simple route for testing Render deployment
@app.route("/")
def hello():
    return "Hello World - Flask is working on Render!"

# Set up paths so the app can find your project folders (static/templates)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.join(BASE_DIR, 'Sky_Hub_Project')

# Tell Flask where to look for your existing frontend files
app.template_folder = os.path.join(PROJECT_DIR, 'templates')
app.static_folder = os.path.join(PROJECT_DIR, 'static')

if __name__ == "__main__":
    # Get port from environment or default to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
