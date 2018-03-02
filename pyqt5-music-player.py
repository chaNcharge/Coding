import sys
from PyQt5.QtCore import QUrl, QDirIterator
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QMenuBar, QAction, QHBoxLayout, QVBoxLayout
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaPlayer, QMediaContent


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.player = QMediaPlayer()
        self.playlist = QMediaPlaylist()
        self.menubar = QMenuBar()
        self.title = 'PyQt5 music player'
        self.left = 300
        self.top = 300
        self.width = 300
        self.height = 150
        self.initUI()

    def initUI(self):
        # Add file menu
        filemenu = self.menubar.addMenu('File')
        filemenu.addAction(self.fileOpen())
        filemenu.addAction(self.folderOpen())

        self.addControls()

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def addControls(self):
        # Add song controls
        playBtn = QPushButton('Play')  # play button
        pauseBtn = QPushButton('Pause')  # pause button
        stopBtn = QPushButton('Stop')  # stop button
        volumeDescBtn = QPushButton('V (-)')  # Decrease Volume
        volumeIncBtn = QPushButton('V (+)')  # Increase Volume
        # Add playlist controls
        prevBtn = QPushButton('Prev Song')
        nextBtn = QPushButton('Next Song')
        # Add button layouts
        controlArea = QVBoxLayout()  # centralWidget
        controls = QHBoxLayout()
        playlistCtrlLayout = QHBoxLayout()
        # Add buttons to song controls layout
        controls.addWidget(volumeDescBtn)
        controls.addWidget(playBtn)
        controls.addWidget(pauseBtn)
        controls.addWidget(stopBtn)
        controls.addWidget(volumeIncBtn)
        # Add buttons to playlist controls layout
        playlistCtrlLayout.addWidget(prevBtn)
        playlistCtrlLayout.addWidget(nextBtn)
        # Add to vertical layout
        controlArea.addLayout(controls)
        controlArea.addLayout(playlistCtrlLayout)
        self.setLayout(controlArea)

    def fileOpen(self):
        fileAc = QAction('Open File', self)
        fileAc.setShortcut('Ctrl+O')
        fileAc.setStatusTip('Open File')
        fileAc.triggered.connect(self.openFile)
        return fileAc

    def openFile(self):
        print("File button clicked!")
        song = QFileDialog.getOpenFileName(
            self, "Open Song", "~", "Sound Files (*.mp3)")
        print(song[0])

        url = QUrl.fromLocalFile(song[0])
        self.playlist.addMedia(QMediaContent(url))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)

        self.player.setPlaylist(self.playlist)
        self.player.playlist().setCurrentIndex(0)
        self.player.play()

    def folderOpen(self):
        folderAc = QAction('Open Folder', self)
        folderAc.setShortcut('Ctrl+D')
        folderAc.setStatusTip(
            'Open Folder (Will add all the files in the folder) ')
        folderAc.triggered.connect(self.addFiles)
        return folderAc

    def addFiles(self):
        folderChosen = QFileDialog.getExistingDirectory(
            self, 'Open Music Folder', '~')
        if folderChosen != None:
            it = QDirIterator(folderChosen)
            it.next()
            while it.hasNext():
                if it.fileInfo().isDir() == False and it.filePath() != '.':
                    fInfo = it.fileInfo()
                    print(it.filePath(), fInfo.suffix())
                    if fInfo.suffix() in ('mp3', 'ogg', 'wav', 'm4a'):
                        print('added file', fInfo.fileName())
                        self.playlist.addMedia(QMediaContent(
                            QUrl.fromLocalFile(it.filePath())))
                it.next()
            self.player.setPlaylist(self.playlist)
            self.player.playlist().setCurrentIndex(0)
            self.player.play()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
