import sys
import os

# Add your application directory to the Python path
# This might be redundant if python-path is set correctly in WSGIDaemonProcess,
# but it doesn't hurt and provides a fallback.
sys.path.insert(0, '/home/hbdghd/web/efficiency100percent.com/public_html/flask_app/flask_app')

# Optional: Add the site-packages from your virtual environment directly if needed
# This is usually handled by python-home, but can be a fallback for debugging.
sys.path.insert(0, '/home/hbdghd/web/efficiency100percent.com/public_html/flask_app/flask_app/env/lib/python3.8/site-packages')
# (Replace X with your Python minor version, e.g., python3.9)

# Activate the virtual environment - often not strictly necessary with WSGIPythonHome/python-home
# but some setups might benefit.


from main import app as application # Replace 'your_flask_app_module'
                                                # with the actual name of your Flask app's Python file
                                                # e.g., 'main_app' if your app is in main_app.py
