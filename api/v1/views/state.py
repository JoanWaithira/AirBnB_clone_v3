#!/usr/bin/python3
"""
A view for State objects
"""
from api.v1.views import state_view
from models import storage
from models.state import State
from flask import make_response, jsonify


@state_view.route("/api/v1/states", methods=['GET'], strict_slashes=False)
def states():
    """retrieves a list of state objects"""
    payload = {}
    for obj in storage.all(State).values():
        payload.update(obj.to_dict())
    response = make_response(jsonify(payload), 200)
    response.headers['Content-Type'] = 'application/json'
    return response
