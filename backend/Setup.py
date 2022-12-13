from flask import Flask
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
# sets up user credentials for spotify api
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

@app.route('/recently-played', methods=['GET'])
def recently_played():
    # gets recently played songs
    results = sp.current_user_recently_played()
    return results

@app.route('/top-tracks', methods=['GET'])
def top_tracks():
    # gets top tracks
    results = sp.current_user_top_tracks()
    return results
if __name__ == '__main__':
    app.run(debug=True)