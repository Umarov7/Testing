import os, sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
os.system('clear')
# import index as s_w
# class Project(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setMaximumSize(1840,1000)
#         self.setMinimumSize(1840,1000)
#         self.setStyleSheet('background: rgb(227,249,136);')

#         self.main_btn = QPushButton('Second window',self)
#         self.main_btn.setGeometry(1480,920,300,50)
#         self.main_btn.setFont(QFont('Poor Richard',22))
#         self.main_btn.setStyleSheet('''border-color: rgb(0,128,128);
#         border-style: dotted;
#         border-width: 3px;
#         border-radius: 15px;
#         background-color: rgb(127,255,212);
#         color: rgb(217,0,76);''')
#         self.main_btn.clicked.connect(self.click_main)

#         self.txt = QTextEdit(self)
#         self.txt.move(800,100)
#         self.txt.resize(400,200)
#         self.txt.setFont(QFont('',20))
#         self.txt.setStyleSheet('''border: 2px solid black; border-radius: 15px;''')
#         self.txt.setAlignment(Qt.AlignCenter)
    
#     def click_main(self):
#         self.window = s_w.Second_Window()
#         self.window.lb.setText(self.txt.toPlainText())
#         self.window.show()
#         self.hide()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     p = Project()
#     p.show()
#     sys.exit(app.exec_())