from SpotifyView import SpotifyMainView
class SpotifyCtrl:
    def __init__(self, model, view):
        self.get_data = model
        self.view = view

        self.connect_signals()


    def save_son(self):
        self.get_data.save_songs()
        self.view.dlabel.setText('Songs Saved')
        print('hello')

    def restore_songs(self):
        pass

    def connect_signals(self):
        print('hello')
        self.view.save.clicked.connect(self.save_son)  # filler code here
        self.view.restore.clicked.connect(self.restore_songs)  # filler code here

