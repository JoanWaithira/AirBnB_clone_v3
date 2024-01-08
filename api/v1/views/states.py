#!/usr/bin/python3
"""
A view for State objects
"""
from api.v1.views import app_views
from models import storage
from models.state import State
from flask import make_response, jsonify, abort, request


@app_views.route("/states", methods=['GET', 'POST'], strict_slashes=False)
def states():
    """retrieves a list of state objects"""
    if request.method == 'GET':
        states_list = []
        for obj in storage.all(State).values():
            states_list.append(obj.to_dict())
        return jsonify(states_list), 200

    elif request.method == 'POST':
        new_dict = request.get_json()
        if not request.is_json:
            abort(400, description='Not a JSON')
        if 'name' not in new_dict:
            abort(400, description='Missing name')
        new_state = State(**new_dict)
        storage.new(new_state)
        storage.save()
        return jsonify(new_state.to_dict()), 201


@app_views.route("/states/<state_id>",
                 methods=['GET', 'DELETE', 'POST', 'PUT'],
                 strict_slashes=False)
def get_state(state_id):
    """retrieves state by id"""
    obj = storage.get(State, str(state_id))
    if request.method == 'GET':
        if obj:
            return jsonify(obj.to_dict())
        else:
            abort(404)
    elif request.method == 'DELETE':
        if obj:
            storage.delete(obj)
            storage.save()
            return jsonify({}), 200
        else:
            abort(404)
    elif request.method == 'PUT':
        obj = storage.get(State, str(state_id))
        if not obj:
            abort(404)
        new_dict = request.get_json()
        if not request.is_json:
            abort(400, description='Not a JSON')
        for key, val in new_dict.items():
            if key != 'id' or key != 'created_at' or key != 'updated_at':
                setattr(obj, key, val)
        storage.save()
        return obj.to_dict(), 200
