import sys
from PyQt5.QtCore import QUrl, QDirIterator
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QFileDialog, QMenuBar, QAction, QHBoxLayout, QVBoxLayout
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaPlayer, QMediaContent


class App(QMainWindow):

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
        self.userAction = -1  # 0- stopped, 1- playing 2-paused
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
        wid = QWidget(self)
        self.setCentralWidget(wid)
        # Add song controls
        playBtn = QPushButton('Play')  # play button
        pauseBtn = QPushButton('Pause')  # pause button
        stopBtn = QPushButton('Stop')  # stop button
        volumeDescBtn = QPushButton('V (-)')  # Decrease Volume
        volumeIncBtn = QPushButton('V (+)')  # Increase Volume
        # Add playlist controls
        prevBtn = QPushButton('Prev Song')
        shuffleBtn = QPushButton('Shuffle')
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
        playlistCtrlLayout.addWidget(shuffleBtn)
        playlistCtrlLayout.addWidget(nextBtn)
        # Add to vertical layout
        controlArea.addLayout(controls)
        controlArea.addLayout(playlistCtrlLayout)
        wid.setLayout(controlArea)
        # Connect each button to their appriate function
        volumeDescBtn.clicked.connect(self.decreaseVolume)
        playBtn.clicked.connect(self.playhandler)
        pauseBtn.clicked.connect(self.pausehandler)
        stopBtn.clicked.connect(self.stophandler)
        volumeIncBtn.clicked.connect(self.increaseVolume)

        prevBtn.clicked.connect(self.prevSong)
        shuffleBtn.clicked.connect(self.shufflelist)
        nextBtn.clicked.connect(self.nextSong)

    def fileOpen(self):
        fileAc = QAction('Open File', self)
        fileAc.setShortcut('Ctrl+O')
        fileAc.setStatusTip('Open File')
        fileAc.triggered.connect(self.openFile)
        return fileAc

    def openFile(self):
        print("File button clicked!")
        song = QFileDialog.getOpenFileName(self, "Open Song", "~", "Sound Files (*.mp3)")
        print(song[0])

        url = QUrl.fromLocalFile(song[0])
        self.playlist.addMedia(QMediaContent(url))
        print(self.playlist.mediaCount())

        self.player.setPlaylist(self.playlist)
        self.player.play()
        self.userAction = 1

    def folderOpen(self):
        folderAc = QAction('Open Folder', self)
        folderAc.setShortcut('Ctrl+D')
        folderAc.setStatusTip('Open Folder (Will add all the files in the folder) ')
        folderAc.triggered.connect(self.addFiles)
        return folderAc

    def addFiles(self):
        print("Folder button clicked!")
        if self.playlist.mediaCount() != 0:
            self.folderIterator()
            print(self.playlist.mediaCount())
        else:
            self.folderIterator()
            self.player.setPlaylist(self.playlist)
            self.player.playlist().setCurrentIndex(0)
            self.player.play()
            print(self.playlist.mediaCount())
            self.userAction = 1
    
    def folderIterator(self):
        folderChosen = QFileDialog.getExistingDirectory(self, 'Open Music Folder', '~')
        if folderChosen != None:
            it = QDirIterator(folderChosen)
            it.next()
            while it.hasNext():
                if it.fileInfo().isDir() == False and it.filePath() != '.':
                    fInfo = it.fileInfo()
                    print(it.filePath(), fInfo.suffix())
                    if fInfo.suffix() in ('mp3', 'ogg', 'wav', 'm4a'):
                        print('added file', fInfo.fileName())
                        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(it.filePath())))
                it.next()
            if it.fileInfo().isDir() == False and it.filePath() != '.':
                fInfo = it.fileInfo()
                print(it.filePath(), fInfo.suffix())
                if fInfo.suffix() in ('mp3', 'ogg', 'wav', 'm4a'):
                    print('added file', fInfo.fileName())
                    self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(it.filePath())))
    
    def playhandler(self):
        self.userAction = 1
        if self.player.state() == QMediaPlayer.StoppedState :
            if self.player.mediaStatus() == QMediaPlayer.NoMedia:
                print(self.playlist.mediaCount())
                if self.playlist.mediaCount() == 0:
                    self.openFile()
                    self.player.play()
                if self.playlist.mediaCount() != 0:
                    self.player.setPlaylist(self.playlist)
            elif self.player.mediaStatus() == QMediaPlayer.LoadedMedia:
                self.player.play()
            elif self.player.mediaStatus() == QMediaPlayer.BufferedMedia:
                self.player.play()
        elif self.player.state() == QMediaPlayer.PausedState:
            self.player.play()

    def pausehandler(self):
        self.userAction = 2
        self.player.pause()

    def stophandler(self):
        self.userAction = 0
        self.player.stop()
        self.playlist.clear()
        print("Playlist cleared!")
        
    def increaseVolume(self):
        vol = self.player.volume()
        vol = min(vol+5,100)
        self.player.setVolume(vol)
        
    def decreaseVolume(self):
        vol = self.player.volume()
        vol = max(vol-5,0)
        self.player.setVolume(vol)

    def prevSong(self):
        if self.playlist.mediaCount() == 0:
            self.openFile()
        elif self.playlist.mediaCount() != 0:
            self.player.playlist().previous()
    
    def shufflelist(self):
        self.playlist.shuffle()
        print("Shuffled playlist!")

    def nextSong(self):
        if self.playlist.mediaCount() == 0:
            self.openFile()
        elif self.playlist.mediaCount() != 0:
            self.player.playlist().next()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
