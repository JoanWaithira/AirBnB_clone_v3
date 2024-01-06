#!/usr/bin/python3
"""index.py"""
from api.v1.views import app_views


@app_views.route("/status")
def status():
    return f'{"status": "OK"}'
