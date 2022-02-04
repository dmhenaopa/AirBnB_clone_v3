#!/usr/bin/python3
"""
   New User object that handles all
   default RESTFul API actions
"""
from flask import request
from api.v1.app import *
from api.v1.views.index import *
from models.user import User
import json


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """Return json file with all USERS"""
    new_dict = storage.all('User')
    new_array = []
    for user in new_dict.values():
        new_array.append(user.to_dict())
    return json.dumps(new_array)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """Return json file of object User, filtered with id"""
    new_dict = storage.get(User, user_id)
    if new_dict is None:
        return error_handler_404(new_dict)
    else:
        return json.dumps(new_dict.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_user(user_id):
    """Delete an object User by id"""
    object = storage.get(User, user_id)
    if object is None:
        return error_handler_404(object)
    else:
        storage.delete(object)
        storage.save()
        return jsonify({}), 200


@app_views.route('/users',
                 methods=['POST'], strict_slashes=False)
def create_user():
    """Create a new object User"""
    try:
        request_data = request.get_json()
    except Exception:
        return error_handler_400("Not a JSON")

    if 'email' not in request_data:
        return error_handler_400("Missing email")

    elif 'password' not in request_data:
        return error_handler_400("Missing password")

    information = dict(request_data)
    new_user = User(**information)
    storage.new(new_user)

    new_json = json.dumps(new_user.to_dict())
    storage.save()
    return new_json, 201


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """Update information of an object User by id"""
    object = storage.get(User, user_id)
    if object is None:
        return error_handler_404(object)

    try:
        request_data = request.get_json()
    except Exception:
        return error_handler_400("Not a JSON")

    ignore = ["id", "created_at", "updated_at", "email"]
    for key, value in dict(request_data).items():
        if key not in ignore:
            setattr(object, key, value)

    new_json = json.dumps(object.to_dict())
    storage.save()
    return new_json, 200
