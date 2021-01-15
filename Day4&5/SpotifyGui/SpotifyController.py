from SpotifyView import SpotifyMainView
import time
import functools
class SpotifyCtrl:
    def __init__(self, model, view):
        self.get_data = model
        self.view = view

        self.connect_signals()

    def _saveSong(self):
        self.view.setDisplayText('Saving Songs - Please Wait')
        self.get_data.save_songs()
        self.view.setDisplayText('Songs saved')

    def _setDisplayText(self, text):
        self.view.setDisplayText(text)

    def restore_songs(self):
        print('hi')

    def connect_signals(self):
        self.view.save.clicked.connect(functools.partial(self._saveSong))  # filler code here
        self.view.restore.clicked.connect(functools.partial(self.restore_songs))  # filler code here

