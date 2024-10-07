import os, sys, mysql.connector as mc, bcrypt
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from hashlib import sha256
os.system('clear')

class Sign(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Website')
        self.setWindowIcon(QIcon('/home/ibrohim/Downloads/reg.ico'))
        self.setFixedSize(1200,600)
        self.setFont(QFont('',21))

        self.bn_in = QPushButton('Sign in',self)
        self.bn_in.setGeometry(100,50,150,50)
        self.bn_in.setStyleSheet('border: 3px solid black')
        self.bn_in.clicked.connect(self.sign_in)

        self.bn_up = QPushButton('Sign up',self)
        self.bn_up.setGeometry(950,50,150,50)
        self.bn_up.setStyleSheet('border: 3px solid black')
        self.bn_up.clicked.connect(self.sign_up)
    def sign_in(self):
        pass
    def sign_up(self):
        pass
if __name__ == '__main__':
    app = QApplication(sys.argv)
    s = Sign()
    s.show()
    sys.exit(app.exec_())