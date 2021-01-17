from SpotifyView import SpotifyMainView
from SpotifyModel import SpotifyModel
from SpotifyController import SpotifyCtrl
from PyQt5.QtWidgets import QApplication
import sys
# Client code
def main():
    """Main function."""
    # Create an instance of QApplication
    spotify_app = QApplication(sys.argv)
    # Show the Spotify GUI
    view = SpotifyMainView()
    model = SpotifyModel()



    # Create instances of the model and the controller

    SpotifyCtrl(model=model, view=view)

    view.show()
    # Execute the calculator's main loop
    sys.exit(spotify_app.exec_())


if __name__ == '__main__':
    main()
