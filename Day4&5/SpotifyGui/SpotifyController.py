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
        folder = self.view.chooseFile()
        self.get_data.save_songs(folder)
        self.view.setDisplayText('Songs saved')

    def _setDisplayText(self, text):
        self.view.setDisplayText(text)

    def restore_songs(self):
        pass

    def connect_signals(self):
        self.view.save.clicked.connect(functools.partial(self._saveSong))
        self.view.restore.clicked.connect(functools.partial(self.restore_songs))

