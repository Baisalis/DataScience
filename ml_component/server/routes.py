# ml_component/server/routes.py
from ml_component.server import app as API, db 
from flask import request, jsonify, make_response


@API.route('/api/v1/')
def index():
    responseJson = {
        'status': 'success',
        'message': 'Welcome to the ml_component of the Spotify Song Suggester!'
    }
    return make_response(jsonify(responseJson)), 200