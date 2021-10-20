import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = 'e8276e07cedb4aa1aa6ffa7c1e70b899'
secret = '3e31c59da81c4d28bea32e35a2ba78aa'

CMM = SpotifyClientCredentials(client_id=cid client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=CMM)
