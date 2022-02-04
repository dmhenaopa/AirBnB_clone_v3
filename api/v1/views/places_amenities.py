#!/usr/bin/python3
"""
   New view for the link between
   Place objects and Amenity objects
   that handles all default RESTFul API actions
"""
from flask import request
from api.v1.app import *
from api.v1.views.index import *
from models.amenity import Amenity
from models.place import Place
import json


@app_views.route('/places/<place_id>/amenities',
                 methods=['GET'], strict_slashes=False)
def get_place_amenities(place_id):
    """Return json file with all AMENITIES"""
    new_dict = storage.get('Place', place_id)
    new_array = []
    if new_dict:
        for amenity in new_dict.amenities:
            new_array.append(amenity.to_dict())
        return json.dumps(new_array)
    else:
        return error_handler_404(new_dict)


@app_views.route('/places/<place_id>/amenities/<amenity_id>',
                 methods=['DELETE', 'POST'], strict_slashes=False)
def delete_place_amenity(place_id, amenity_id):
    """Delete an object Amenity by place_id"""
    flag = False
    place_object = storage.get(Place, place_id)
    if place_object is None:
        return error_handler_404(place_object)

    amenity_object = storage.get(Amenity, amenity_id)
    if amenity_object is None:
        return error_handler_404(amenity_object)
    if request.method == 'DELETE':
        for amenity in place_object.amenities:
            if amenity.id == amenity_id:
                flag = True
                break
        if flag:
            place_object.amenities.remove(amenity_object)
            storage.save()
            return jsonify({}), 200
        return error_handler_404(object)
    else:
        for amenity in place_object.amenities:
            if amenity.id == amenity_id:
                return json.dumps(amenity_object.to_dict()), 200
        place_object.amenities.append(amenity_object)
        new_json = json.dumps(amenity_object.to_dict())
        storage.save()
        return new_json, 201
