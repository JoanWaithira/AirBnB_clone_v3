#!/usr/bin/python3
"""Your first endpoint (route) will be to return the status of your API"""

from flask import Flask, jsonify, make_response
from models import storage
from api.v1.views import app_views
import os
app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_context(exception=None):
    """cleanup"""
    storage.close()


@app.errorhandler(404)
def not_found(Exception=None):
    payload = {"error": "Not found"}
    response = make_response(jsonify(payload), 404)
    response.headers['Content-Type'] = 'application/json'
    return response


if __name__ == '__main__':
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True, debug=True)
