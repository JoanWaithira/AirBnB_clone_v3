#!/usr/bin/python3
"""A view for cities"""
from api.v1.views import app_views
from models.state import State
from models.city import City
from models import storage
from flask import jsonify, abort, request


@app_views.route("/states/<state_id>/cities",
                 methods=['GET', 'POST'], strict_slashes=False)
def get_state_cities(state_id):
    """Retrieves City objects of a state"""
    state = storage.get(State, str(state_id))
    if not state or len(state.cities) == 0:
        abort(404)
    if request.method == 'GET':
        return jsonify([city.to_dict() for city in state.cities])
    if request.method == 'POST':
        new_dict = request.get_json()
        if not request.is_json:
            abort(400, description="Not a JSON")
        if 'name' not in new_dict:
            abort(400, description="Missing name")
        new_city = City(**new_dict)
        setattr(new_city, 'state_id', state_id)
        storage.new(new_city)
        storage.save()
        return jsonify(new_city.to_dict())


@app_views.route("/cities/<city_id>",
                 methods=['GET', 'DELETE', 'PUT'], strict_slashes=False)
def get_city(city_id):
    """retrieves a City object"""
    city = storage.get(City, str(city_id))
    if not city:
        abort(404)
    if request.method == 'GET':
        return jsonify(city.to_dict())
    if request.method == ['DELETE']:
        storage.delete(city)
        storage.save()
        return jsonify({}), 200
    if request.method == 'PUT':
        new_dict = request.get_json()
        if not request.is_json:
            abort(400, description="Not a JSON")
        for key, val in new_dict.items():
            if key != 'created_at' or key != 'updated_at' or key != 'id':
                setattr(city, key, val)
        storage.save()
        return jsonify(city.to_dict()), 200
