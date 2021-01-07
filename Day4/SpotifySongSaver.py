import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import json
# scope = 'user-library-read'
scope = 'playlist-read-private'
with open('spotifySettings.json', 'r') as f:
    keys = json.load(f)

def show_tracks(results):
    for item in results['items']:
        track = item['track']
        print("%32.32s %s" % (track['artists'][0]['name'], track['name']))


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=keys['client'],
                                               client_secret=keys['secret'],
                                               redirect_uri="https://google.com/", scope=scope))

id = sp.me()['id']

results = sp.current_user_playlists(limit=50)

for i, playlist in enumerate(results['items']):
    if playlist['owner']['id'].lower() == id.lower():
        print("%d %s" % (i, playlist['name']))


    res = sp.playlist(playlist['id'], fields='tracks')
    tracks = res['tracks']

    # show_tracks(tracks)


    while tracks['next']:
        tracks = sp.next(tracks)
        # print(tracks)
        show_tracks(tracks)





with open('playlistsdata.json', 'w') as f:
    json.dump(results, f, indent=4)

with open('test.json', 'w') as f:
    json.dump(tracks, f, indent=4)
