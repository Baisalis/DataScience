# ml_component/server/routes.py
from ml_component.server import app as API, db 
from ml_component.server.models import Song
from ml_component.server.util import nearest_by_id
from flask import request, jsonify, make_response


@API.route('/api/v1/')
def index():
    responseJson = {
        'status': 'success',
        'message': 'Welcome to the ml_component of the Spotify Song Suggester!'
    }
    return make_response(jsonify(responseJson)), 200


@API.route('/api/v1/song')
def get_songs():
    songs = Song.query.limit(10).all()
    songs = [song.to_json() for song in songs]
    responseJson = {
        'status': 'success',
        'data': songs
    }
    return make_response(jsonify(responseJson)), 200


@API.route('/api/v1/song/<track_id>')
def song_by_track_id(track_id):
    curr_song = Song.query.filter_by(track_id=track_id).first()
    if curr_song:
        responseJson = {
            'status': 'success',
            'data': curr_song.to_json()
        }
        return make_response(jsonify(responseJson)), 200
    else:
        responseJson = {
            'status': 'failure',
            'message': "No Song found with track_id equal to {}".format(track_id)
        }
        return make_response(jsonify(responseJson)), 404


@API.route('/api/v1/recommend/<track_id>')
def recommend_by_track_id(track_id):
    curr_song = Song.query.filter_by(track_id=track_id).first()
    if curr_song:
        print(curr_song.to_json())
        recommendations = nearest_by_id(track_id)
        print("RECS:")
        print(recommendations)
        responseJson = {
            'status': 'success',
            'data': recommendations
        }
        return make_response(jsonify(responseJson)), 200
    else:
        responseJson = {
            'status': 'failure',
            'message': "No Song found with track_id equal to {}, can't make recommendations.".format(track_id)
        }
        return make_response(jsonify(responseJson)), 404