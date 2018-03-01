import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QMenuBar, QAction
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaPlayer, QMediaContent


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.player = QMediaPlayer()
        self.playlist = QMediaPlaylist()
        self.menubar = QMenuBar()
        self.title = 'PyQt5 music player'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        # Add file menu
        filemenu = self.menubar.addMenu('File')
        filemenu.addAction(self.fileOpen())

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def fileOpen(self):
        fileAc = QAction('Open File',self)
        fileAc.setShortcut('Ctrl+O')
        fileAc.setStatusTip('Open File')
        fileAc.triggered.connect(self.openFile)
        return fileAc

    def openFile(self):
        print("File button clicked!")
        song = QFileDialog.getOpenFileName(self, "Open Song", "~/", "Sound Files (*.mp3)")
        print(song[0])
        
        url = QUrl.fromLocalFile(song[0])
        self.playlist.addMedia(QMediaContent(url))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)

        self.player.setPlaylist(self.playlist)
        self.player.playlist().setCurrentIndex(0)
        self.player.play()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())