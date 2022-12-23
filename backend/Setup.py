from flask import Flask, jsonify, redirect, request, session
from flask_cors import CORS
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv
import time

# load environment variables
load_dotenv()

# run flask app and set up cors
app = Flask(__name__)
# generate random secret key
app.secret_key = os.urandom(24)
CORS(app)

# sets up user credentials for spotify api
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")


# get all scopes
scopes = 'user-read-recently-played user-top-read user-read-currently-playing user-read-playback-state user-library-read streaming'

# authenticates user and sends react app to url
@app.route('/authenticate', methods=['GET'])
def authenticate_user():
    sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id, client_secret, redirect_uri, scope=scopes, show_dialog=True)
    auth_url = sp_oauth.get_authorize_url()
    return jsonify({'url': auth_url})

# gets access token from spotify api
@app.route('/callback')
def callback():
    
    # gets access token from spotify api
    sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id, client_secret, redirect_uri, scope=scopes)
    session.clear()
    # gets code from query string
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    # Saving the access token along with all other token related info
    session['token_info'] = token_info
    return redirect('http://localhost:3000/')

# gets recently played songs
@app.route('/recently-played', methods=['GET'])
def recently_played():
    # sp gets the spotipy api object with the spotify client credentials which are the client id and client secret
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    # gets recently played songs
    results = sp.current_user_recently_played(limit=20)
    # returns results so that it can be used in the react app.
    return jsonify(results)
    

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
