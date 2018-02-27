import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 music player'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        button = QPushButton("Button", self)
        button.setToolTip("Example button")
        button.move(100, 70)
        button.clicked.connect(self.onClick)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

    def onClick(self):
        print("Button clicked!")
        dir_ = QFileDialog.getExistingDirectory(None, 'Select a folder:', '/', QFileDialog.ShowDirsOnly)
        print(dir_)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())