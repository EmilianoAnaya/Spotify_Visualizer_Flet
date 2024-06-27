from spotipy.oauth2 import SpotifyOAuth
import spotipy

def get_Spotify(client_id: str=None, client_secret: str=None) -> spotipy:
    spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, 
                                                        client_secret=client_secret, 
                                                        redirect_uri="https://localhost:8888/callback",
                                                        scope="user-read-playback-state"))
    return spotify