#!/usr/bin/python3
"""Blueprint and routes"""
# from api.v1.views import app_views
# from flask import jsonify
# from api.v1.app import storage
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
    return json.dumps(new_array)


# @app_views.route('/states/<states_id>', methods=['GET'])
# def return_status():
#     """Return json file with status"""
#     return jsonify({
#         "status": "OK"
#     })


# @app_views.route('/states/<states_id>', methods=['DELETE'])
# def return_status():
#     """Return json file with status"""
#     return jsonify({
#         "status": "OK"
#     })


# @app_views.route('/states', methods=['POST'])
# def return_status():
#     """Return json file with status"""
#     return jsonify({
#         "status": "OK"
#     })
