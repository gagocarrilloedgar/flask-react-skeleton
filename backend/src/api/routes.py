"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from api.models import User, db
from api.utils import APIException, generate_sitemap
from flask import Blueprint, Flask, jsonify, request, url_for

# Blueprint Configuration is used for grouping routes under a common prefix
api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200
