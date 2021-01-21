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
            try:
                self.get_data.save_playlists_data(folder)
            except Exception as e:
                print(e)
        else:
            pass


        self.view.setDisplayText('Songs saved')

    def _setDisplayText(self, text):
        self.view.setDisplayText(text)

    def delete_songs(self):
        if self.view.reconfirm_delete():
            self.view.setDisplayText('Deleting Playlists - Please Wait')
            self.get_data.delete_all_playlists()
            self.view.setDisplayText('Playlists deleted')


    def restore_songs(self):
        file = self.view.chooseSave()
        if file[0]:
            with open(file[0]) as data:
                if self.view.reconfirm():
                    self.view.setDisplayText('Restoring Songs - Please Wait')
                    self.get_data.restore_playlists(data)
                    # self.get_data.delete_all_playlists()
                    self.view.setDisplayText('Songs restored')



    def connect_signals(self):
        self.view.save.clicked.connect(functools.partial(self._saveSong))
        self.view.restore.clicked.connect(functools.partial(self.restore_songs))
        self.view.delete.clicked.connect(functools.partial(self.delete_songs))

