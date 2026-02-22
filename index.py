import sys
import os

# Get the absolute path of the current directory (Root)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Path to the Sky_Hub_Project folder where app.py resides
PROJECT_DIR = os.path.join(BASE_DIR, 'Sky_Hub_Project')

# Add the project directory to sys.path so it can find models, forms, etc.
sys.path.append(PROJECT_DIR)

from app import app as application

# Explicitly tell Flask where to find templates and static files
application.template_folder = os.path.join(PROJECT_DIR, 'templates')
application.static_folder = os.path.join(PROJECT_DIR, 'static')

app = application
