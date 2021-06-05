import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class LoginWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        userlabel = QLabel(self)
        passlabel = QLabel(self)
        userlabel.move(100, 20)
        passlabel.move(100, 60)
        userlabel.setText('Username:')
        passlabel.setText('Password:')
        username = QLineEdit(self)
        password = QLineEdit(self)
        username.setFixedWidth(200)
        password.setFixedWidth(200)
        username.move(200, 20)
        password.move(200, 60)
        self.statusBar()
        b = QPushButton(self)
        b.clicked.connect(self.buttonClicked)
        b.setText('Enter')
        self.setGeometry(100, 100, 500, 400)
        b.move(200, 100)
        self.setWindowTitle('Login Portal')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.setWindowTitle('Logged In!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    sys.exit(app.exec())
