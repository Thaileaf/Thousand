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

        # self.login = LoginDialog()
        # self.login.exec()

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
        self.file.exec()
        return self.file.selectedFiles()[0]

    def reconfirm(self):
        self.reconfirm_dialog = ReconfirmDialog()
        return self.reconfirm_dialog.exec()

    def chooseSave(self):
        self.save = QFileDialog()
        return self.save.getOpenFileName()

class ReconfirmDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(ReconfirmDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle('Restore Songs')
        self.setFixedSize(300, 100)


        self.layout = QVBoxLayout()

        self.setLayout(self.layout)

        self.label = QLabel()
        self.label.setText('ArE YoU SurE yOu WaNT to resStoRe SongS?')

        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(buttons)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.buttonBox)




class FileDialog(QFileDialog):
    def __init__(self, *args, **kwargs):
        super(FileDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle('Files test')
        self.setFileMode(QFileDialog.Directory)

    def closeEvent(self):
        return 0




