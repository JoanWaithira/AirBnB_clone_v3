#!/usr/bin/python3
"""
A view for State objects
"""
from api.v1.views import app_views
from models import storage
from models.state import State
from flask import make_response, jsonify, abort


@app_views.route("/states", methods=['GET'], strict_slashes=False)
def states():
    """retrieves a list of state objects"""
    payload = {}
    for obj in storage.all(State).values():
        payload.update(obj.to_dict())
    response = make_response(jsonify(payload), 200)
    response.headers['Content-Type'] = 'application/json'
    return response


@app_views.route("/states/<state_id>", methods=['GET'], strict_slashes=False)
def get_state(state_id):
    """retrieves state by id"""
    obj = storage.get(State, str(state_id))
    if obj:
        return jsonify(obj.to_dict())
    else:
        abort(404)
