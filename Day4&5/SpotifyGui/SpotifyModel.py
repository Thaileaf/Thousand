import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import json
import requests
import math
import base64

class SpotifyModel:

    def __init__(self):

        self.scope = 'playlist-read-private playlist-modify-private playlist-modify-public ugc-image-upload'
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
                if(song['is_local'] == False):
                    songs[song['track']['name']] = song['track']['uri']

        tracks = playlist['tracks']
        append_songs(tracks)
        while tracks['next']:
            tracks = self.sp.next(tracks)
            append_songs(tracks)

        return songs

    def save_cover_image(self, playlist_id, path, name):
        img_data = self.sp.playlist_cover_image(playlist_id)
        if img_data:
            url = img_data[0]['url']
            response = requests.get(url=url)
            os.makedirs(path + '/spotify_covers',exist_ok=True)
            file_path = path + f'/spotify_covers/{name}.jpg'
            with open(file_path, 'wb') as f:
                f.write(response.content)



    def save_playlists_data(self, path, name):

        id = self.sp.me()['id']
        results = self.sp.current_user_playlists(limit=50)
        playlists = {}

        def parse_playlist_data(self, results, playlists, path):
            for i, playlist in enumerate(results['items']):
                if playlist['owner']['id'].lower() == id.lower():
                    print("%d %s" % (i, playlist['name']))

                    res = self.sp.playlist(playlist['id'], fields='tracks')
                    playlists[playlist['name']] = {}
                    playlists[playlist['name']]['tracks'] = self.playlist_to_list(res)
                    playlists[playlist['name']]['id'] = playlist['id']
                    playlists[playlist['name']]['private'] = True
                    playlists[playlist['name']]['description'] = playlist['description']

                    self.save_cover_image(playlist['id'], path, playlist['name'])

                else:
                    playlists[playlist['name']] = {'uri': playlist['uri'], 'private': False}

        os.makedirs(path + f'/{name}')
        file_path = path + f"/{name}"
        parse_playlist_data(self, results, playlists, file_path)
        while results['next']:
            results = self.sp.next(results)
            parse_playlist_data(self, results, playlists, path)



        with open(file_path + '/tracks.json', 'w') as f:
            json.dump(playlists, f, indent=4)

    def delete_all_playlists(self):
        results = self.sp.current_user_playlists(limit=50)
        def delete_fifty(results):
            for playlist in results['items']:
                print(playlist['id'])
                self.sp.current_user_unfollow_playlist(playlist['id'])

        delete_fifty(results)
        while results['next']:
            results = self.sp.next(results)
            delete_fifty(results)



        # playlists = []
        # def get_playlists(results):
        #     list = []
        #     for playlist in results['items']:
        #         playlists.append(playlist['id'])
        #         print(playlist['id'])
        #     return list
        # playlists.extend(get_playlists(results))
        # while results['next']:
        #     self.sp.next(results)
        #     playlists.extend(get_playlists(results))


    def restore_playlists(self, path):
        with open(path + '/tracks.json', 'r') as data:
            dict = json.load(data)

        failed = []
        for playlist in dict:
            try:
                if dict[playlist]['private']:
                    playlist_id = self.sp.user_playlist_create(self.sp.me()['id'], playlist, False, False, dict[playlist]['description'])['id']

                    uris = list(dict[playlist]['tracks'].values())

                    if uris:
                        if len(uris) > 100:
                            for i in range(0, math.ceil(len(uris) / 100)):
                                self.sp.playlist_add_items(playlist_id, uris[0+(100*i):99+(100*i)])
                        else:
                            self.sp.playlist_add_items(playlist_id, uris)

                    with open(path + f'/spotify_covers/{playlist}.jpg', 'rb') as pic:
                        encoded_bytes = base64.b64encode(pic.read())
                        encoded_str = str(encoded_bytes)[2:].replace("'",'')

                        self.sp.playlist_upload_cover_image(playlist_id, encoded_str)
            except:
                failed.append(playlist)










    def file_test(self, path):
        playlists = {'test':'test'}
        file_path = path + "/songs.json"
        with open(file_path, 'w') as f:
            json.dump(playlists, f, indent=4)
