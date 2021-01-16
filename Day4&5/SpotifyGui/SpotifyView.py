from PyQt5.QtWidgets import QMainWindow, QDialogButtonBox
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtGui
import time

from PyQt5.QtCore import Qt

class SpotifyMainView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Spotify App converter')
        self.setFixedSize(400, 400)

        self.generalLayout = QVBoxLayout()

        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        self.login = LoginDialog()
        self.login.exec()

        self._createDisplay()

    def _createDisplay(self):
        self.save = QPushButton('Save songs')
        self.restore = QPushButton('Restore songs')

        buttonsLayout = QGridLayout()

        buttonsLayout.addWidget(self.save)
        buttonsLayout.addWidget(self.restore)

        self.generalLayout.addLayout(buttonsLayout)

        self.dlabel = QLabel()
        self.generalLayout.addWidget(self.dlabel)
        self.dlabel.setText('')

    def setDisplayText(self, text):
        self.dlabel.setText(text)
        QApplication.processEvents()

    def chooseFile(self):
        self.file = FileDialog()
        self.file.setFileMode
        self.file.exec()

class LoginDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(LoginDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle('Login')

        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        print(buttons)

        self.buttonBox = QDialogButtonBox(buttons)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.user = QLineEdit()
        self.passW = QLineEdit()
        self.ulabel = QLabel()
        self.ulabel.setText('Username')
        self.plabel = QLabel()
        self.plabel.setText('Password')


        self.user.setFixedHeight(35)
        self.passW.setFixedHeight(35)



        self.layout = QFormLayout()
        self.layout.addWidget(self.ulabel)
        self.layout.addWidget(self.user)
        self.layout.addWidget(self.plabel)
        self.layout.addWidget(self.passW)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

class FileDialog(QFileDialog):
    def __init__(self, *args, **kwargs):
        super(FileDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle('Files')




