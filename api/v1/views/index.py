#!/usr/bin/python3
"""Blueprint and routes"""
from api.v1.views import app_views
from flask import jsonify
from api.v1.app import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.user import User
import json


@app_views.route('/status', methods=['GET'])
def return_status():
    """Return json file with status"""
    return jsonify({
        "status": "OK"
    })


@app_views.route('/stats', methods=['GET'])
def stats():
    """Return number of objects by type"""
    classes = {"amenities": Amenity, "cities": City,
               "places": Place, "reviews": Review, "states": State,
               "users": User}
    new_dict = {}
    for clss in classes:
        count_result = storage.count(classes[clss])
        new_dict[clss] = count_result
    return json.dumps(new_dict)
