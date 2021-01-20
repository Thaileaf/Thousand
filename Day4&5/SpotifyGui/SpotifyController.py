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
        if folder:
            self.get_data.save_playlists_data(folder)
        else:
            pass

        # self.get_data.file_test(folder)

        self.view.setDisplayText('Songs saved')

    def _setDisplayText(self, text):
        self.view.setDisplayText(text)

    def restore_songs(self):
        with open(self.view.chooseSave()[0]) as data:
            if self.view.reconfirm():
                self.get_data.restore_playlists(data)
            else:
                pass

    def connect_signals(self):
        self.view.save.clicked.connect(functools.partial(self._saveSong))
        self.view.restore.clicked.connect(functools.partial(self.restore_songs))

