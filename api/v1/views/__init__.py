#!/usr/bin/python3
"""Blueprint and routes"""
from flask import Blueprint


app_views = Blueprint('app', __name__, url_prefix='/api/v1')
from api.v1.views.index import *
from api.v1.views.states import *
