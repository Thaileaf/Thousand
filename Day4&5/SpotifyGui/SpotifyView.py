from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QLabel

from PyQt5.QtCore import Qt

class SpotifyMainView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Spotify App converter')
        self.setFixedSize(400, 400)

        self.generalLayout = QFormLayout()

        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        self._createDisplay()

    def _createDisplay(self):
        self.user = QLineEdit()
        self.passW = QLineEdit()
        self.ulabel = QLabel

        self.user.setFixedHeight(35)
        self.passW.setFixedHeight(35)

        self.generalLayout.addWidget(self.user)
        self.generalLayout.addWidget(self.passW)






