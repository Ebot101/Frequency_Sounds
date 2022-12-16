import spotipy.util as util
import spotipy
import os
import dotenv

dotenv.load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")

spotipy_auth = spotipy.oauth2.SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)

def get_spotify_auth():
    return spotipy_auth.get_authorize_url()



# Prompt the user to visit the authorization URL and grant access to your application
print("Please visit the following URL and grant access to your Spotify account:")
print(spotipy_auth.get_authorize_url())

# Wait for the user to grant access
print("Waiting for authorization...")

# Get the authorization code from the redirect URI
code = input("Enter the authorization code: ")

# Exchange the code for an access token
token = util.prompt_for_user_token(
    username,
    scope,
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri
)

# Print the access token
print(token)