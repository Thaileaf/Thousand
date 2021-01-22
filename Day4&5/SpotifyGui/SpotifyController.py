from SpotifyView import SpotifyMainView
import time
import functools
import os
class SpotifyCtrl:
    def __init__(self, model, view):
        self.get_data = model
        self.view = view

        self.connect_signals()

    def _saveSong(self):
        name = self.view.inputFile()
        if name:
            folder = self.view.chooseFile()
            if folder:
                self.view.setDisplayText('Saving Songs - Please Wait')
                self.get_data.save_playlists_data(folder, name)
                self.view.setDisplayText('Songs saved')
            else:
                self.view.setDisplayText('')


    def _setDisplayText(self, text):
        self.view.setDisplayText(text)

    def delete_songs(self):
        if self.view.reconfirm_delete():
            self.view.setDisplayText('Deleting Playlists - Please Wait')
            self.get_data.delete_all_playlists()
            self.view.setDisplayText('Playlists deleted')


    def restore_songs(self):
        folder = self.view.chooseFile()
        if folder:
            if self.view.reconfirm():
                self.view.setDisplayText('Restoring Songs - Please Wait')
                self.get_data.restore_playlists(folder)
                # self.get_data.delete_all_playlists()
                self.view.setDisplayText('Songs restored')





    def connect_signals(self):
        self.view.save.clicked.connect(functools.partial(self._saveSong))
        self.view.restore.clicked.connect(functools.partial(self.restore_songs))
        self.view.delete.clicked.connect(functools.partial(self.delete_songs))

