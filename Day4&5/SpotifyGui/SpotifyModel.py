import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import json
import requests


class SpotifyModel:

    def __init__(self):

        self.scope = 'playlist-read-private playlist-modify-private'
        with open('spotifySettings.json', 'r') as f:
            self.keys = json.load(f)

        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.keys['client'],
                                                            client_secret=self.keys['secret'],
                                                            scope=self.scope,
                                                            redirect_uri='http://localhost:8888'))

    def show_tracks_playlist(self, results):
        for item in results['items']:
            track = item['track']
            print("%32.32s %s" % (track['artists'][0]['name'], track['name']))

    def playlist_to_list(self, playlist):
        songs = {}

        def append_songs(tracks):
            for song in tracks['items']:
                try:
                    songs[song['track']['name']] = song['track']['uri']
                except Exception as e:
                    print(e)

        tracks = playlist['tracks']
        append_songs(tracks)
        while tracks['next']:
            tracks = self.sp.next(tracks)
            append_songs(tracks)

        return songs

    def save_cover_image(self, playlist_id, path):
        url = self.sp.playlist_cover_image(playlist_id)[0]['url']
        response = requests.get(url=url)
        os.makedirs(path + '/spotify_covers',exist_ok=True)
        file_path = path + f'/spotify_covers/{playlist_id}.jpg'
        with open(file_path, 'wb') as f:
            f.write(response.content)


    def save_playlists_data(self, path):
        id = self.sp.me()['id']
        results = self.sp.current_user_playlists(limit=50)
        playlists = {}



        for i, playlist in enumerate(results['items']):
            if playlist['owner']['id'].lower() == id.lower():
                print("%d %s" % (i, playlist['name']))

                res = self.sp.playlist(playlist['id'], fields='tracks')
                playlists[playlist['name']] = {}
                playlists[playlist['name']]['tracks'] = self.playlist_to_list(res)
                playlists[playlist['name']]['id'] = playlist['id']
                playlists[playlist['name']]['private'] = True
                try:
                    playlists[playlist['name']]['description'] = playlist['description']
                except Exception as e:
                    print(e)
                    print(playlist)
                self.save_cover_image(playlist['id'], path)

            else:
                playlists[playlist['name']] = {'uri':playlist['uri'], 'private':False}


        file_path = path + "/songs.json"
        with open(file_path, 'w') as f:
            json.dump(playlists, f, indent=4)

    def restore_playlists(self, data):
        # for playlist in data:
        #     if playlist['private']:
        #         self.sp.user_playlist_create(self.sp.me()['id'], playlist, False, False, playlist['description'])

        self.sp.user_playlist_create(self.sp.me()['id'], 'test_playlist', False, False, 'test description')


    def file_test(self, path):
        playlists = {'test':'test'}
        file_path = path + "/songs.json"
        with open(file_path, 'w') as f:
            json.dump(playlists, f, indent=4)
