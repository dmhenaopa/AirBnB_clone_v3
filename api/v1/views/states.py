#!/usr/bin/python3
"""Blueprint and routes"""
from flask import request, abort, jsonify
from api.v1.app import *
from api.v1.views.index import *
from models.state import State
import json


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """Return json file with all STATES"""
    new_dict = storage.all(State)
    new_array = []
    for object in new_dict.values():
        new_array.append(object.to_dict())
    return jsonify(new_array)
    return json.dumps(new_array)


@app_views.route('/states/<states_id>', methods=['GET'], strict_slashes=False)
def get_state(states_id):
    """Return json file of object State, filtered with id"""
    new_dict = storage.get(State, states_id)
    if new_dict is None:
        return abort(404)
    else:
        return json.dumps(new_dict.to_dict())


@app_views.route('/states/<states_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(states_id):
    """Delete an object State by id"""
    object = storage.get(State, states_id)
    if object is None:
        return abort(404)
    storage.delete(object)
    storage.save()
    return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """Create a new object State"""
    request_data = request.get_json()
    if not request_data:
        return error_handler_400("Not a JSON")
    if 'name' not in request_data:
        return error_handler_400("Missing name")
    info_state = dict(request_data)
    new_state = State(**request_data)
    # storage.new(new_state)
    new_json = json.dumps(new_state.to_dict())
    new_state.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<states_id>', methods=['PUT'], strict_slashes=False)
def update_state(states_id):
    """Update information of an object State by id"""
    object = storage.get(State, states_id)
    if object is None:
        return abort(404)
    request_data = request.get_json()
    if not request_data:
        return error_handler_400("Not a JSON")
    ignore = ["id", "created_at", "updated_at"]
    for key, value in dict(request_data).items():
        if key not in ignore:
            setattr(object, key, value)
    new_json = json.dumps(object.to_dict())
    storage.save()
    return new_json, 200
