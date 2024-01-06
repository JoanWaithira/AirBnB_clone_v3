#!/usr/bin/python3
"""index.py"""
from api.v1.views import app_views
from flask import jsonify, make_response


@app_views.route("/status", strict_slashes=False)
def status():
    payload = {"status": "OK"}
    response = make_response(jsonify(payload), 200)
    response.headers['Content-Type'] = 'application/json'
    return response
