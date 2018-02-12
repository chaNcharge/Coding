import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 template'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        button = QPushButton("Button", self)
        button.setToolTip("Example button")
        button.move(100, 70)
        button.clicked.connect(self.onClick)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage("Running!")

        buttonReply = QMessageBox.question(self, 'Question 1', 'Is my processor fat?')
        if buttonReply == QMessageBox.Yes:
            print("They hate me >:(")
        elif buttonReply == QMessageBox.No:
            print("Good, I'm not slacking.")

        self.show()

    def onClick(self):
        print("Buddon clicked!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
