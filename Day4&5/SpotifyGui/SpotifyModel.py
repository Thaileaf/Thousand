import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import json


class SpotifyModel:

    def __init__(self):

        self.scope = 'playlist-read-private'
        with open('spotifySettings.json', 'r') as f:
            self.keys = json.load(f)

        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.keys['client'],client_secret=self.keys['secret'],
                                                            scope=self.scope,
                                                            redirect_uri='https://www.google.com'))

    def show_tracks_playlist(self, results):
        for item in results['items']:
            track = item['track']
            print("%32.32s %s" % (track['artists'][0]['name'], track['name']))

    def playlist_to_list(self, playlist):
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
            tracks = self.sp.next(tracks)
            append_songs(tracks)

        return songs


    def save_playlists_data(self, path):
        id = self.sp.me()['id']
        results = self.sp.current_user_playlists(limit=50)
        playlists = {}

        for i, playlist in enumerate(results['items']):
            if playlist['owner']['id'].lower() == id.lower():
                print("%d %s" % (i, playlist['name']))

                res = self.sp.playlist(playlist['id'], fields='tracks')
                playlists[playlist['name']] = self.playlist_to_list(res)
            else:
                playlists[playlist['name']] = playlist['uri']




        file_path = path + "/songs.json"
        with open(file_path, 'w') as f:
            json.dump(playlists, f, indent=4)


    def file_test(self, path):
        playlists = {'test':'test'}
        file_path = path + "/songs.json"
        with open(file_path, 'w') as f:
            json.dump(playlists, f, indent=4)
