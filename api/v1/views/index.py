#!/usr/bin/python3
"""index.py"""

from api.v1.views import app_views
from flask import jsonify, make_response
from models import storage
from models.city import City
from models.place import Place
from models.user import User
from models.review import Review
from models.state import State
from models.amenity import Amenity


@app_views.route("/status", methods=['GET'], strict_slashes=False)
def status():
    payload = {"status": "OK"}
    response = make_response(jsonify(payload), 200)
    response.headers['Content-Type'] = 'application/json'
    return response


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def get_stats():
    """Get the number of each object type."""
    stats = {
        'amenities': storage.count(Amenity),
        'cities': storage.count(City),
        'places': storage.count(Place),
        'reviews': storage.count(Review),
        'states': storage.count(State),
        'users': storage.count(User),
    }
    response = make_response(jsonify(stats), 200)
    response.headers['Content-Type'] = 'application/json'
    return response
