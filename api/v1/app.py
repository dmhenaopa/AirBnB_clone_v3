#!/usr/bin/python3
"""app module - endpoints"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


app.register_blueprint(app_views)


@app.teardown_appcontext
def close(self):
    """Method that calls storage close method"""
    storage.close()


@app.errorhandler(404)
def error_handler_404(self):
    """Method that returns a JSON-formatted
       404 status code
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(400)
def error_handler_400(self):
    """Method that returns a JSON-formatted
       400 status code
    """
    return jsonify({"error": self}), 400


if __name__ == "__main__":
    app.run(host=getenv("HBNB_API_HOST"),
            port=getenv("HBNB_API_PORT"),
            threaded=True)
