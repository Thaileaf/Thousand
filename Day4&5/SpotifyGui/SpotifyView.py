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
from PyQt5 import Qt
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
        self.delete = QPushButton('Delete playlists')

        buttonsLayout = QGridLayout()

        buttonsLayout.addWidget(self.save)
        buttonsLayout.addWidget(self.restore)
        buttonsLayout.addWidget(self.delete)

        self.generalLayout.addLayout(buttonsLayout)

        self.dlabel = QLabel()
        self.generalLayout.addWidget(self.dlabel)
        self.dlabel.setText('')

    def setDisplayText(self, text):
        self.dlabel.setText(text)
        QApplication.processEvents()

    def inputFile(self):
        self.file_name_dialog = SetFileNameDialog(title='Save',
                                                  dialog='Name of File?')
        self.file_name_dialog.exec()
        return 'test'

    def chooseFile(self):
        self.file = FileDialog(title='Choose Folder to Save')
        self.file.setFileMode(QFileDialog.DirectoryOnly)
        return self.file.selectedFiles()[0] if self.file.exec() else 0


    def reconfirm(self):
        self.reconfirm_dialog = ReconfirmDialog(title='Restore playlists',
                                                dialog='Are you sure you want to restore playlists')
        return self.reconfirm_dialog.exec()

    def reconfirm_delete(self):
        self.reconfirm_dialog = ReconfirmDialog(title='Delete playlists',
                                                dialog='Are you sure you want to delete all playlists?')
        return self.reconfirm_dialog.exec()

    def chooseSave(self):
        self.save = FileDialog(title='Choose Selected File')
        self.save.setAcceptMode(QFileDialog.AcceptOpen)

        return self.save.getOpenFileName()[0] if self.save.exec() else 0

class ReconfirmDialog(QDialog):
    def __init__(self, title, dialog, *args, **kwargs):
        super(ReconfirmDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle(title)
        self.setFixedSize(300, 100)


        self.layout = QVBoxLayout()

        self.setLayout(self.layout)

        self.label = QLabel()
        self.label.setText(dialog)

        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(buttons)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.buttonBox)

class SetFileNameDialog(ReconfirmDialog):
    def __init__(self, *args, **kwargs):
        super(SetFileNameDialog, self).__init__(*args, **kwargs)
        self.name = QLineEdit()
        self.name.setAlignment(Qt.AlignLeft)
        self.layout.insertWidget(0, self.name)





class FileDialog(QFileDialog):
    def __init__(self, title, *args, **kwargs):
        super(FileDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle(title)

    def reject(self):
        print('hi')
        super().reject()





