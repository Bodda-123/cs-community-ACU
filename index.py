import os
import sys

# 1) Get the absolute path of the project folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.join(BASE_DIR, 'Sky_Hub_Project')

# 2) Add the project directory to sys.path so Python can find app.py, models, etc.
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

# 3) Import the real Flask app from Sky_Hub_Project/app.py
try:
    from app import app as application
except ImportError:
    # Fallback if imports are still tricky on some environments
    sys.path.append(os.getcwd())
    from Sky_Hub_Project.app import app as application

# 4) Configure folders for static and templates
application.template_folder = os.path.join(PROJECT_DIR, 'templates')
application.static_folder = os.path.join(PROJECT_DIR, 'static')

app = application

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
