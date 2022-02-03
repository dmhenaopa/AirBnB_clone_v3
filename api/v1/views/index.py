#!/usr/bin/python3
"""Blueprint and routes"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def return_status():
    """Return json file with status"""
    return jsonify({
        "status": "OK"
    })
