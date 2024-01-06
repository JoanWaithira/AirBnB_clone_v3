#!/usr/bin/python3
"""Your first endpoint (route) will be to return the status of your API"""

from flask import Flask
from models import storage
from api.v1.views import app_views
app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_context():
    """cleanup"""
    storage.close()
