import os, sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
os.system('clear')
class Tasbeh(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tasbeh')
        self.setWindowIcon(QIcon('/home/ibrohim/Downloads/icon_tasbeeh.ico'))
        self.setFixedSize(500,400)
        self.setStyleSheet('Background: #20B2AA')
        self.index = 0
        self.zikrlar = ('Subhanalloh','Alhamdulillah','Allohuakbar')

        self.vBox = QVBoxLayout()
        self.zikr = QLabel(self.zikrlar[0])
        self.count = QLineEdit('0')
        self.bn = QPushButton("📿")
        self.vBox.addWidget(self.zikr)
        self.vBox.addWidget(self.count)
        self.vBox.addWidget(self.bn)
        self.setLayout(self.vBox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Tasbeh()
    window.show()
    sys.exit(app.exec_())