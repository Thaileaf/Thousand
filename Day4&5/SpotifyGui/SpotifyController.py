from SpotifyView import SpotifyMainView
class SpotifyCtrl:
    def __init__(self, model, view):
        self.get_data = model
        self.view = view

        self.connect_signals()


    def connect_signals(self):
        self.view.save.clicked.connect(pass) #filler code here
        self.view.restore.clicked.connect(pass) #filler code here

