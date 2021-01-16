import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import os
import json
# scope = 'user-library-read'
scope = 'playlist-read-private'
with open('spotifySettings.json', 'r') as f:
    keys = json.load(f)

def show_tracks_playlist(results):
    for item in results['items']:
        track = item['track']
        print("%32.32s %s" % (track['artists'][0]['name'], track['name']))

def playlist_to_list(playlist):
    songs = []

    def append_songs(tracks):
        for song in tracks['items']:
            try:
                songs.append((song['track']['name'], song['track']['uri']))
            except Exception as e:
                print(e)

    tracks = playlist['tracks']
    append_songs(tracks)
    while tracks['next']:
        tracks = sp.next(tracks)
        append_songs(tracks)

    return songs


client_cred_manager = SpotifyClientCredentials(client_id=keys['client'], client_secret=keys['secret'])
sp = spotipy.Spotify(client_credentials_manager=client_cred_manager)

id = sp.me()['id']


results = sp.current_user_playlists(limit=50)
playlists = {}

for i, playlist in enumerate(results['items']):
    if playlist['owner']['id'].lower() == id.lower():
        print("%d %s" % (i, playlist['name']))

        res = sp.playlist(playlist['id'], fields='tracks')
        playlists[playlist['name']] = playlist_to_list(res)
    else:
        playlists[playlist['name']] = playlist['uri']





with open('playlistsdata.json', 'w') as f:
    json.dump(results, f, indent=4)

with open('test.json', 'w') as f:
    json.dump(playlists, f, indent=4)
