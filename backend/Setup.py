from flask import Flask, jsonify, redirect, request
from flask_cors import CORS
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv
import sqlite3
import spotipy.util as util

load_dotenv()

app = Flask(__name__)
CORS(app)
# sets up user credentials for spotify api
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

@app.route('/authenticate', methods=['GET'])
def authenticate_user():
    spotipy_oauth = spotipy.oauth2.SpotifyOAuth(client_id, client_secret, redirect_uri)
    auth_url = spotipy_oauth.get_authorize_url()
    return jsonify({'url': auth_url})

@app.route('/callback')
def callback():
    code = request.args.get('code')
    print(code)
    return 'handled'

if __name__ == '__main__':
    app.run(host='localhost', port=5000)

# @app.route('/recently-played', methods=['GET'])
# def recently_played():
#     # gets recently played songs
#     results = sp.current_user_recently_played()
#     return results

# # @app.route('/top-tracks', methods=['GET'])
# def top_tracks(term = None):
#     # gets top tracks
#     results = sp.current_user_top_tracks(time_range=term)
#     return results
    

# print(recently_played())
