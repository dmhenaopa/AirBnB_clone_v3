#!/usr/bin/python3
"""
   New view for the link between
   Place objects and Amenity objects
   that handles all default RESTFul API actions
"""
from flask import request
from api.v1.app import error_handler, error_handler_400
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
        return error_handler(new_dict)


@app_views.route('/places/<place_id>/amenities/<amenity_id>',
                 methods=['DELETE', 'POST'], strict_slashes=False)
def delete_amenity(place_id, amenity_id):
    """Delete an object Amenity by place_id"""
    flag = False
    place_object = storage.get(Place, place_id)
    if place_object is None:
        return error_handler(place_object)

    amenity_object = storage.get(Amenity, amenity_id)
    if amenity_object is None:
        return error_handler(amenity_object)

    for amenity in place_object.amenities:
        if amenity.id == amenity_id:
            flag = True
            break

    if flag:
        if request.method == 'DELETE':
            storage.delete(object)
            storage.save()
            return jsonify({}), 200
        else:
            dictionary = {}
            dictionary['id'] = amenity_id
            new_amenity = Amenity(**dictionary)
            storage.new(new_amenity)
            new_json = json.dumps(new_amenity.to_dict())
            storage.save()
            return new_json, 201

    return error_handler(object)
