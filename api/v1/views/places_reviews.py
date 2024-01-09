#!/usr/bin/python3
"""View for Review objects"""

from flask import jsonify, request, abort
from models import storage
from models.place import Place
from models.review import Review
from models.user import User
from api.v1.views import app_views


@app_views.route("/places/<place_id>/reviews", methods=['GET', 'POST'], strict_slashes=False)
def places_reviews(place_id):
    """gets reviews of a place"""
    reviews_list = []
    if len(storage.all(Place)) != 0:
        for obj in storage.all(Place).values():
            if obj.id == place_id:
                reviews_list.append(obj.reviews)
    if len(reviews_list) == 0:
        abort(404)
    if request.method == 'GET':
        return jsonify([review.to_dict() for review in reviews_list]), 200
    if request.method == 'POST':
        new_dict = request.get_json(silent=True)
        if not new_dict:
            abort(400, 'Not a JSON')
        if 'user_id' not in new_dict:
            abort(400, 'Missing user_id')
        if 'text' not in new_dict:
            abort(400, 'Missing text')
        if not storage.get(User, new_dict['user_id']):
            abort(404)
        new_review = Review(**new_dict)
        storage.new(new_review)
        storage.save()
        return jsonify(new_review.to_dict()), 200


@app_views.route("/reviews/<review_id>", methods=['GET', 'DELETE', 'PUT'], strict_slashes=False)
def get_review(review_id):
    review_obj = storage.get(Review, review_id)
    if not review_obj:
        abort(404)
    if request.method == 'GET':
        return jsonify(review_obj.to_dict()), 200
    if request.method == 'DELETE':
        storage.delete(review_obj)
        storage.save()
        return jsonify({}), 200
    if request.method == 'PUT':
        new_dict = request.get_json(silent=True)
        if not new_dict:
            abort(400, 'Not a JSON')
        for key, val in new_dict.items():
            if key not in ['created_at', 'updated_at', 'user_id', 'id']:
                setattr(review_obj, key, val)
        return jsonify(review_obj.to_dict()), 200
