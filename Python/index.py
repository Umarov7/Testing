import os, sys, random
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import mysql.connector as mc

from hashlib import sha256
import bcrypt

from queue import Queue

from heapq import *
os.system('clear')
'''
class App(QMainWindow):
    __count = 0
    def __init__(self,x = 800, y = 600):
        super().__init__()
        self.setGeometry(100,80,x,y)
        self.setWindowTitle("My first PyQt project")
        self.setWindowIcon(QIcon("/home/ibrohim/Downloads/python_logo_icon.ico"))
        self.lb = QLabel('Foundation N50',self)
        self.lb.move(200,300)
        self.lb.resize(800,200)
        self.lb.setFont(QFont('Consolas',56))
        self.btn = QPushButton("Click me",self)
        self.btn.setGeometry(500,510,250,50)
        self.btn.setFont(QFont("Calibri",22))
        self.btn.setStyleSheet("""
            border-style: solid;
            border-width: 3px;
            border-color: rgb(0,255,0);
            border-radius: 25px;
            background-color: rgb(0,0,0);
            color: rgb(0,255,0);""")
        self.btn.clicked.connect(self.btn_click)

    def btn_click(self):
        App.__count += 1
        if App.__count % 2:
            self.btn.setText(self.lb.text())
        else:
            self.btn.setText('Click me')
        print(self.btn.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_on = App(1200,800)
    app_on.show()
    sys.exit(app.exec_())
'''
'''
class Programme(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,400,800,600)
        self.setWindowTitle('Login')
        self.setWindowIcon(QIcon("/home/ibrohim/Downloads/lp.ico"))
        self.setMaximumSize(800,600)
        self.setMinimumSize(800,600)
        self.setStyleSheet("""
            background-color: rgb(64,224,208);""")
        self.lblogin = QLabel('Enter email: ',self)
        self.lblogin.setGeometry(100,50,250,50)
        self.lblogin.setFont(QFont('Poor Richard',18))
        self.lblogin.setStyleSheet("color: rgb(0,0,128)")

        self.txtlogin = QLineEdit(self)
        self.txtlogin.setGeometry(360,50,300,50)
        self.txtlogin.setFont(QFont("Consolas",18))
        self.txtlogin.setStyleSheet("""
            border-style: inset;
            border-width: 2px;
            border-radius: 15px;
            border-color: rgb(0,255,0);
            color: blue;
            background-color: rgb(225,228,205);
        """)
        self.txtlogin.setAlignment(Qt.AlignCenter)

        self.lbpass = QLabel('Enter password: ',self)
        self.lbpass.setGeometry(100,110,250,50)
        self.lbpass.setFont(QFont('Poor Richard',18))
        self.lbpass.setStyleSheet("color: rgb(0,0,128)")

        self.txtpass = QLineEdit(self)
        self.txtpass.setGeometry(360,110,300,50)
        self.txtpass.setFont(QFont("Consolas",18))
        self.txtpass.setStyleSheet("""
            border-style: inset;
            border-width: 2px;
            border-radius: 15px;
            border-color: rgb(0,255,0);
            color: blue;
            background-color: rgb(225,228,205);
        """)
        self.txtpass.setAlignment(Qt.AlignCenter) 
        self.txtpass.setEchoMode(QLineEdit.Password)

        self.bn = QPushButton('Enter',self)
        self.bn.setGeometry(280,210,250,50)
        self.bn.setFont(QFont("Poor Richard",18))
        self.bn.setStyleSheet("""
            border-style: solid;
            border-width: 3px;
            border-color: rgb(241,196,15);
            border-radius: 25px;
            background-color: rgb(0,0,0);
            color: rgb(241,196,15);""")
        self.bn.clicked.connect(self.bn_click)
        
    def bn_click(self):
        if self.txtlogin.text() == 'Ibrohim' and self.txtpass.text() == 'Umarov':
            print(f'Email: {self.txtlogin.text()}\nPassword: {self.txtpass.text()}')
            self.txtlogin.setText('')
            self.txtpass.clear()
            self.bn.setText('Exit')
        else:
            print('Wrong email or password')

app = QApplication(sys.argv)
project = Programme()
project.show()
sys.exit(app.exec_())
'''



"""
class Program(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMaximumSize(600,400)
        self.setMinimumSize(600,400)
        self.setWindowTitle('Messabox')
        self.setWindowIcon(QIcon('/home/ibrohim/Downloads/icon_message.ico'))
        
        self.setFont(QFont('Poor Richard',24))
        self.lbl = QLabel('Enter name:',self)
        self.lbl.setGeometry(20,50,250,50)
        
        self.txt = QLineEdit(self)
        self.txt.resize(250,50)
        self.txt.move(275,50)
        self.txt.setStyleSheet('''border: 2px solid lime;
        border-radius: 15px;''')
        self.txt.setAlignment(Qt.AlignRight)

        self.btn = QPushButton('Submit',self)
        self.btn.setGeometry(300,105,200,50)
        self.btn.setStyleSheet('''border-color: rgb(0,0,255);
        border-radius: 15px;
        border-style: solid;
        border-width: 2px;
        background-color: rgb(0,0,128);
        color: rgb(255,255,224);''')
        self.btn.clicked.connect(self.click_btn)

    def click_btn(self):
        msg = QMessageBox(self)
        msg.setText(f'Hello {self.txt.text()}! Do you wanna exit?')
        msg.setFont(QFont('Consolas',20))
        msg.setWindowTitle('M E S S A G E')
        msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        msg.buttonClicked.connect(self.message)
        msg.setIcon(QMessageBox.Question)
        msg.show()
    def message(self,x):39
        if x.text() == '&Yes':
            exit()
        else:
            print('The programme has not been finished')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pr = Program()
    pr.show()
    sys.exit(app.exec_())
"""
'''
class Countries(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(900,700)
        self.setWindowTitle('Countries')
        self.setWindowIcon(QIcon('/home/ibrohim/Downloads/icon_worldmap.ico'))

        self.setFont(QFont('Consolas',24))
        self.lb = QLabel(self)
        self.lb.setGeometry(100,150,700,500)
        self.lb.setStyleSheet('border: 3px solid black')
        self.cmb = QComboBox(self)
        self.cmb.setGeometry(20,50,350,50)
        self.cmb.addItems(['UK','Italy','Germany','France'])
        self.cmb.currentIndexChanged.connect(self.display_image)
        
    def display_image(self):
        path = self.cmb.currentText()
        url = f'/home/ibrohim/Downloads/{path}.jpg'
        self.lb.setPixmap(QPixmap(url).scaled(700, 500, Qt.KeepAspectRatio))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    c = Countries()
    c.show()
    sys.exit(app.exec_())
'''




# 5-month
"""
import main_window as mw
class Second_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMaximumSize(1840,1000)
        self.setMinimumSize(1840,1000)
        self.setStyleSheet('background: rgb(227,249,236);')

        self.s_btn = QPushButton('Main window',self)
        self.s_btn.setGeometry(20,920,300,50)
        self.s_btn.setFont(QFont('Poor Richard',22))
        self.s_btn.setStyleSheet('''border-color: rgb(230,128,128);
        border-style: solid;
        border-width: 3px;
        border-radius: 15px;
        background-color: rgb(127,255,212);
        color: rgb(0,28,120);''')
        self.s_btn.clicked.connect(self.click_second)

        self.lb = QLabel(self)
        self.lb.setGeometry(670,250,500,250)
        self.lb.setFont(QFont('Calibri',26))
        self.lb.setStyleSheet('''border: 3px solid lime; border-radius: 20px; color: pink;''')
    
    def click_second(self):
        self.w = mw.Project()
        self.w.show()
        self.hide()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    s = Second_Window()
    s.show()
    sys.exit(app.exec_())
"""
'''
class project(QMainWindow):
    __count = 0
    def __init__(self):
        super().__init__()
        self.setFont(QFont('',18))
        self.setFixedSize(1840,1000)
        self.bar = self.menuBar()
        self.txt_col = None
        self.txt_font = None

        open_file = QAction(QIcon('/home/ibrohim/Downloads/icon_open.ico'),'Open File',self)
        open_file.setShortcut('Ctrl+O')
        open_file.triggered.connect(self.open_f)

        save_file = QAction(QIcon('/home/ibrohim/Downloads/icon_save.ico'),'Save File',self)
        save_file.setShortcut('Ctrl+S')
        save_file.triggered.connect(self.save_f)

        edit_colour = QAction(QIcon('/home/ibrohim/Downloads/icon_colour.ico'),'Edit Colour',self)
        edit_colour.setShortcut('Ctrl+R')
        edit_colour.triggered.connect(self.edit_c)

        edit_font = QAction(QIcon('/home/ibrohim/Downloads/icon_font.ico'),'Edit Font',self)
        edit_font.setShortcut('Ctrl+F')
        edit_font.triggered.connect(self.edit_f)
        
        file = self.bar.addMenu('File')
        file.setFont(QFont('Consolas',18))

        file.addActions([open_file,save_file])
        file.addSeparator()
        edit = file.addMenu('Edit')
        edit.setFont(QFont('Consolas',18))
        edit.addAction(edit_colour)
        edit.addAction(edit_font)

        ex = self.bar.addMenu('Exit')
        ex_a = QAction(QIcon('/home/ibrohim/Downloads/icon_exit.ico'),'Exit the programme',self)
        ex_a.setShortcut('Ctrl+E')
        ex_a.triggered.connect(self.end)
        ex.addAction(ex_a)
        ex.setFont(QFont('',18))
        
        self.txt = QTextEdit(self)
        self.txt.setGeometry(320,100,1200,800)

    def open_f(self):
        f_name = QFileDialog.getOpenFileName(self,'Opening a file','/home/ibrohim/Downloads')[0]
        print(f_name)
        f = open(f_name,'rt')
        dt = f.read()
        self.txt.setText(dt)
    def save_f(self):
        project.__count += 1
        fName = QFileDialog.getSaveFileName(self, 'Saving a file')[0]
        print(fName)
        f2 = open(fName,'w')
        f2.write(f'Text Color: {self.txt_col}\n')
        f2.write(f'Text Font: {self.txt_font.toString()}\n')
        f2.write(self.txt.toPlainText())
        f2.close()
        print('New file saved')
    def edit_c(self):
        c = QColorDialog.getColor()
        self.txt.setStyleSheet(f'color: {c.name()};')
        self.txt_col = c.name()
    def edit_f(self):
        f = QFontDialog.getFont()
        if f[1]:
            self.txt.setFont(QFont(f[0]))
            self.txt_font = QFont(f[0])
    def end(self):
        exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    p = project()
    p.show()
    sys.exit(app.exec_())
'''




"""class Game(QMainWindow):
    __numbers = set()
    __attempt = 0
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tag Game')
        self.setWindowIcon(QIcon('/home/ibrohim/Downloads/icon_game.ico'))
        self.setFixedSize(1200,600)
        self.setFont(QFont('',26))

        self.lb = QLabel('Number of attempts:',self)
        self.lb.setGeometry(500,200,400,50)

        self.tablo = QSpinBox(self)
        self.tablo.setGeometry(910,200,150,55)
        self.tablo.setValue(0)
        self.tablo.setMaximum(999)
        self.tablo.setEnabled(False)
        self.tablo.setStyleSheet('''color: rgb(0,255,0);
        border: 2px solid rgb(0,255,0);
        border-radius: 15px;
        background-color: rgb(0,0,0);''')

        self.btn1 = self.button_maker('1',self)
        self.btn1.move(50,50)

        self.btn2 = self.button_maker('2',self)
        self.btn2.move(150,50)

        self.btn3 = self.button_maker('3',self)
        self.btn3.move(250,50)

        self.btn4 = self.button_maker('4',self)
        self.btn4.move(350,50)

        self.btn5 = self.button_maker('5',self)
        self.btn5.move(50,150)

        self.btn6 = self.button_maker('6',self)
        self.btn6.move(150,150)

        self.btn7 = self.button_maker('7',self)
        self.btn7.move(250,150)

        self.btn8 = self.button_maker('8',self)
        self.btn8.move(350,150)

        self.btn9 = self.button_maker('9',self)
        self.btn9.move(50,250)

        self.btn10 = self.button_maker('10',self)
        self.btn10.move(150,250)

        self.btn11 = self.button_maker('11',self)
        self.btn11.move(250,250)

        self.btn12 = self.button_maker('12',self)
        self.btn12.move(350,250)

        self.btn13 = self.button_maker('13',self)
        self.btn13.move(50,350)

        self.btn14 = self.button_maker('14',self)
        self.btn14.move(150,350)

        self.btn15 = self.button_maker('15',self)
        self.btn15.move(250,350)

        self.btn16 = self.button_maker('',self)
        self.btn16.move(350,350)

        self.__ls_btn = [self.btn1,self.btn2,self.btn3,self.btn4,self.btn5,self.btn6,self.btn7,self.btn8,
        self.btn9,self.btn10,self.btn11,self.btn12,self.btn13,self.btn14,self.btn15,self.btn16]
        
        self.functions = [self.btn1_click,self.btn2_click,self.btn3_click,self.btn4_click,self.btn5_click,self.btn6_click,
        self.btn7_click,self.btn8_click,self.btn9_click,self.btn10_click,self.btn11_click,self.btn12_click,
        self.btn13_click,self.btn14_click,self.btn15_click,self.btn16_click]

        self.start_game()

        for x,y in zip(self.__ls_btn,self.functions):
            x.clicked.connect(y)

        self.new_game = self.button_maker('New game',self)
        self.new_game.setGeometry(600,320,250,55)
        self.new_game.clicked.connect(self.start_game)

    def button_maker(self,x,y):
        btn = QPushButton(x,y)
        btn.resize(100,100)
        btn.setStyleSheet('''color: rgb(0,255,128);
        border: 2px solid rgb(0,255,0);
        background-color: rgb(0,0,96);''')
        return btn
        
    def start_game(self):
        Game.__attempt = 0
        while len(Game.__numbers) != 15:
            Game.__numbers.add(random.randint(1,15))
        numbers = list(Game.__numbers)
        random.shuffle(numbers)
        for x,y in zip(self.__ls_btn,numbers):
            x.setText(str(y))
        self.btn16.setText('')
        self.tablo.setValue(0)

    
    def btn1_click(self):
        Game.__attempt += 1
        if self.btn2.text() == '':
            self.btn2.setText(self.btn1.text())
            self.btn1.setText('')
        elif self.btn5.text() == '':
            self.btn5.setText(self.btn1.text())
            self.btn1.setText('')
        else:
            Game.__attempt -= 1
            msg = QMessageBox(self)
            msg.setWindowTitle('E R R O R')
            msg.setText('Movement unavailable')
            msg.setIcon(QMessageBox.Critical)
            msg.setFont(QFont('Calibri',18))
            msg.show()
        self.tablo.setValue(Game.__attempt)
    def btn2_click(self):
        Game.__attempt += 1
        if self.btn1.text() == '':
            self.btn1.setText(self.btn2.text())
            self.btn2.setText('')
        elif self.btn6.text() == '':
            self.btn6.setText(self.btn2.text())
            self.btn2.setText('')
        elif self.btn3.text() == '':
            self.btn3.setText(self.btn2.text())
            self.btn2.setText('')
        else:
            Game.__attempt -= 1
            msg = QMessageBox(self)
            msg.setWindowTitle('E R R O R')
            msg.setText('Movement unavailable')
            msg.setIcon(QMessageBox.Critical)
            msg.setFont(QFont('Calibri',18))
            msg.show()
        self.tablo.setValue(Game.__attempt)
    def btn3_click(self):
        Game.__attempt += 1
        if self.btn2.text() == '':
            self.btn2.setText(self.btn3.text())
            self.btn3.setText('')
        elif self.btn4.text() == '':
            self.btn4.setText(self.btn3.text())
            self.btn3.setText('')
        elif self.btn7.text() == '':
            self.btn7.setText(self.btn3.text())
            self.btn3.setText('')
        else:
            Game.__attempt -= 1
            msg = QMessageBox(self)
            msg.setWindowTitle('E R R O R')
            msg.setText('Movement unavailable')
            msg.setIcon(QMessageBox.Critical)
            msg.setFont(QFont('Calibri',18))
            msg.show()
        self.tablo.setValue(Game.__attempt)
    def btn4_click(self):
        Game.__attempt += 1
        if self.btn3.text() == '':
            self.btn3.setText(self.btn4.text())
            self.btn4.setText('')
        elif self.btn8.text() == '':
            self.btn8.setText(self.btn4.text())
            self.btn4.setText('')
        else:
            Game.__attempt -= 1
            msg = QMessageBox(self)
            msg.setWindowTitle('E R R O R')
            msg.setText('Movement unavailable')
            msg.setIcon(QMessageBox.Critical)
            msg.setFont(QFont('Calibri',18))
            msg.show()
        self.tablo.setValue(Game.__attempt)
    def btn5_click(self):
        Game.__attempt += 1
        if self.btn1.text() == '':
            self.btn1.setText(self.btn5.text())
            self.btn5.setText('')
        elif self.btn6.text() == '':
            self.btn6.setText(self.btn5.text())
            self.btn5.setText('')
        elif self.btn9.text() == '':
            self.btn9.setText(self.btn5.text())
            self.btn5.setText('')
        else:
            Game.__attempt -= 1
            msg = QMessageBox(self)
            msg.setWindowTitle('E R R O R')
            msg.setText('Movement unavailable')
            msg.setIcon(QMessageBox.Critical)
            msg.setFont(QFont('Calibri',18))
            msg.show()
        self.tablo.setValue(Game.__attempt)
    def btn6_click(self):
        Game.__attempt += 1
        if self.btn5.text() == '':
            self.btn5.setText(self.btn6.text())
            self.btn6.setText('')
        elif self.btn2.text() == '':
            self.btn2.setText(self.btn6.text())
            self.btn6.setText('')
        elif self.btn7.text() == '':
            self.btn7.setText(self.btn6.text())
            self.btn6.setText('')
        elif self.btn10.text() == '':
            self.btn10.setText(self.btn6.text())
            self.btn6.setText('')
        else:
            Game.__attempt -= 1
            msg = QMessageBox(self)
            msg.setWindowTitle('E R R O R')
            msg.setText('Movement unavailable')
            msg.setIcon(QMessageBox.Critical)
            msg.setFont(QFont('Calibri',18))
            msg.show()
        self.tablo.setValue(Game.__attempt)
    def btn7_click(self):
        Game.__attempt += 1
        if self.btn6.text() == '':
            self.btn6.setText(self.btn7.text())
            self.btn7.setText('')
        elif self.btn3.text() == '':
            self.btn3.setText(self.btn7.text())
            self.btn7.setText('')
        elif self.btn8.text() == '':
            self.btn8.setText(self.btn7.text())
            self.btn7.setText('')
        elif self.btn11.text() == '':
            self.btn11.setText(self.btn7.text())
            self.btn7.setText('')
        else:
            Game.__attempt -= 1
            msg = QMessageBox(self)
            msg.setWindowTitle('E R R O R')
            msg.setText('Movement unavailable')
            msg.setIcon(QMessageBox.Critical)
            msg.setFont(QFont('Calibri',18))
            msg.show()
        self.tablo.setValue(Game.__attempt)
    def btn8_click(self):
        Game.__attempt += 1
        if self.btn7.text() == '':
            self.btn7.setText(self.btn8.text())
            self.btn8.setText('')
        elif self.btn4.text() == '':
            self.btn4.setText(self.btn8.text())
            self.btn8.setText('')
        elif self.btn12.text() == '':
            self.btn12.setText(self.btn8.text())
            self.btn8.setText('')
        else:
            Game.__attempt -= 1
            msg = QMessageBox(self)
            msg.setWindowTitle('E R R O R')
            msg.setText('Movement unavailable')
            msg.setIcon(QMessageBox.Critical)
            msg.setFont(QFont('Calibri',18))
            msg.show()
        self.tablo.setValue(Game.__attempt)
    def btn9_click(self):
        Game.__attempt += 1
        if self.btn5.text() == '':
            self.btn5.setText(self.btn9.text())
            self.btn9.setText('')
        elif self.btn10.text() == '':
            self.btn10.setText(self.btn9.text())
            self.btn9.setText('')
        elif self.btn13.text() == '':
            self.btn13.setText(self.btn9.text())
            self.btn9.setText('')
        else:
            Game.__attempt -= 1
            msg = QMessageBox(self)
            msg.setWindowTitle('E R R O R')
            msg.setText('Movement unavailable')
            msg.setIcon(QMessageBox.Critical)
            msg.setFont(QFont('Calibri',18))
            msg.show()
        self.tablo.setValue(Game.__attempt)
    def btn10_click(self):
        Game.__attempt += 1
        if self.btn9.text() == '':
            self.btn9.setText(self.btn10.text())
            self.btn10.setText('')
        elif self.btn6.text() == '':
            self.btn6.setText(self.btn10.text())
            self.btn10.setText('')
        elif self.btn11.text() == '':
            self.btn11.setText(self.btn10.text())
            self.btn10.setText('')
        elif self.btn14.text() == '':
            self.btn14.setText(self.btn10.text())
            self.btn10.setText('')
        else:
            Game.__attempt -= 1
            msg = QMessageBox(self)
            msg.setWindowTitle('E R R O R')
            msg.setText('Movement unavailable')
            msg.setIcon(QMessageBox.Critical)
            msg.setFont(QFont('Calibri',18))
            msg.show()
        self.tablo.setValue(Game.__attempt)
    def btn11_click(self):
        Game.__attempt += 1
        if self.btn10.text() == '':
            self.btn10.setText(self.btn11.text())
            self.btn11.setText('')
        elif self.btn7.text() == '':
            self.btn7.setText(self.btn11.text())
            self.btn11.setText('')
        elif self.btn12.text() == '':
            self.btn12.setText(self.btn11.text())
            self.btn11.setText('')
        elif self.btn15.text() == '':
            self.btn15.setText(self.btn11.text())
            self.btn11.setText('')
        else:
            Game.__attempt -= 1
            msg = QMessageBox(self)
            msg.setWindowTitle('E R R O R')
            msg.setText('Movement unavailable')
            msg.setIcon(QMessageBox.Critical)
            msg.setFont(QFont('Calibri',18))
            msg.show()
        self.tablo.setValue(Game.__attempt)
    def btn12_click(self):
        Game.__attempt += 1
        if self.btn11.text() == '':
            self.btn11.setText(self.btn12.text())
            self.btn12.setText('')
        elif self.btn8.text() == '':
            self.btn8.setText(self.btn12.text())
            self.btn12.setText('')
        elif self.btn16.text() == '':
            self.btn16.setText(self.btn12.text())
            self.btn12.setText('')
        else:
            Game.__attempt -= 1
            msg = QMessageBox(self)
            msg.setWindowTitle('E R R O R')
            msg.setText('Movement unavailable')
            msg.setIcon(QMessageBox.Critical)
            msg.setFont(QFont('Calibri',18))
            msg.show()
        self.tablo.setValue(Game.__attempt)
    def btn13_click(self):
        Game.__attempt += 1
        if self.btn9.text() == '':
            self.btn9.setText(self.btn13.text())
            self.btn13.setText('')
        elif self.btn14.text() == '':
            self.btn14.setText(self.btn13.text())
            self.btn13.setText('')
        else:
            Game.__attempt -= 1
            msg = QMessageBox(self)
            msg.setWindowTitle('E R R O R')
            msg.setText('Movement unavailable')
            msg.setIcon(QMessageBox.Critical)
            msg.setFont(QFont('Calibri',18))
            msg.show()
        self.tablo.setValue(Game.__attempt)
    def btn14_click(self):
        Game.__attempt += 1
        if self.btn13.text() == '':
            self.btn13.setText(self.btn14.text())
            self.btn14.setText('')
        elif self.btn10.text() == '':
            self.btn10.setText(self.btn14.text())
            self.btn14.setText('')
        elif self.btn15.text() == '':
            self.btn15.setText(self.btn14.text())
            self.btn14.setText('')
        else:
            Game.__attempt -= 1
            msg = QMessageBox(self)
            msg.setWindowTitle('E R R O R')
            msg.setText('Movement unavailable')
            msg.setIcon(QMessageBox.Critical)
            msg.setFont(QFont('Calibri',18))
            msg.show()
        self.tablo.setValue(Game.__attempt)
    def btn15_click(self):
        Game.__attempt += 1
        if self.btn14.text() == '':
            self.btn14.setText(self.btn15.text())
            self.btn15.setText('')
        elif self.btn11.text() == '':
            self.btn11.setText(self.btn15.text())
            self.btn15.setText('')
        elif self.btn16.text() == '':
            self.btn16.setText(self.btn15.text())
            self.btn15.setText('')
        else:
            Game.__attempt -= 1
            msg = QMessageBox(self)
            msg.setWindowTitle('E R R O R')
            msg.setText('Movement unavailable')
            msg.setIcon(QMessageBox.Critical)
            msg.setFont(QFont('Calibri',18))
            msg.show()
        self.tablo.setValue(Game.__attempt)
    def btn16_click(self):
        Game.__attempt += 1
        if self.btn15.text() == '':
            self.btn15.setText(self.btn16.text())
            self.btn16.setText('')
        elif self.btn12.text() == '':
            self.btn12.setText(self.btn16.text())
            self.btn16.setText('')
        else:
            Game.__attempt -= 1
            msg = QMessageBox(self)
            msg.setWindowTitle('E R R O R')
            msg.setText('Movement unavailable')
            msg.setIcon(QMessageBox.Critical)
            msg.setFont(QFont('Calibri',18))
            msg.show()
        self.tablo.setValue(Game.__attempt)
    
    def check_game(self):
        win = True
        for x in range(len(self.__ls_btn)):
            if self.__ls_btn[x].text() == str(x+1):
                continue
            else:
                win = False
                break
        if win:
            msg = QMessageBox(self)
            msg.setWindowTitle('S U C C E S S')
            msg.setText(f'You\'ve won at {Game.__attempt} attempts')
            msg.setIcon(QMessageBox.Information)
            msg.setFont(QFont('Calibri',18))
            msg.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    g = Game()
    g.show()
    sys.exit(app.exec_())"""




'''
class Database:
    db = None
    def __init__(self):
        self.con = mc.connect(host = "localhost",user = "root",password = "root.702")
    def create_db(self,dbName):
        self.cur = self.con.cursor()
        self.cur.execute(f'Create database if not exists {dbName}')
        self.con.commit()
        Database.db = dbName
    def create_table(self,tb):
        if Database.db is not None:
            self.con = mc.connect(host = "localhost",user = "root",password = "root.702",database = f'{Database.db}')
            self.cur = self.con.cursor()
            sql = f'Create table if not exists {tb}(id int primary key auto_increment,brand varchar(30),price int,speed float,gpu bool)'
            self.cur.execute(sql)
            self.con.commit()
        else:
            print('Database not found')
    def add_info(self,tb):
        n = input('Enter brand/model: ')
        p = int(input('Enter its price: '))
        s = float(input('Enter its speed: '))
        g = int(input('Enter availability of GPU: '))
        self.con = mc.connect(host = 'localhost',user = 'root',password = 'root.702',database = f'{Database.db}')
        self.cur = self.con.cursor()
        sql = f'insert into {tb}(brand,price,speed,gpu) values(%s,%s,%s,%s)'
        self.cur.execute(sql,(n,p,s,g))
        self.con.commit()
    def show_info(self,tb):
        self.con = mc.connect(host = 'localhost',user = 'root',password = 'root.702',database = f'{Database.db}')
        self.cur = self.con.cursor()
        sql = 'select * from {}'.format(tb)
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for x in res:
            print(x)


db = Database()
db.create_db('tech')
db.create_table('laptop')
# db.add_info('laptop')
db.show_info('laptop')
'''




'''
def isPrime(n:int)-> bool:
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
def last_prime(ls:list):
    res = None
    for x in ls:
        if isPrime(x) == True:
            res = x
    return res
ls = list(map(int,input('Enter numbers: ').split()))
print(f'Last prime number: {last_prime(ls)}')
'''
"""
def binary_search(ls,n,b,e):
    if b > e:
        return -1
    else:
        m = (b+e) // 2
        if ls[m] > n:
            return binary_search(ls,n,b,m-1)
        elif ls[m] < n:
            return binary_search(ls,n,m+1,e)
        else:
            return m

numbers = [random.randint(10,99) for x in range(10)]
print(numbers)
numbers.sort()
print(numbers)
target = int(input('Enter a target: '))
res = binary_search(numbers,target,0,len(numbers)-1)
if res == -1:
    print('Not found')
else:
    print(f'Position: {res}')
"""





'''def hash_function(data):
    return hash(data)
s = input('Enter a string: ')
n = input('Enter a number: ')
print(f'Value: {s} - Hash code: {hash_function(s)}')
print(f'Value: {n} - Hash code: {hash_function(n)}')'''

def hash_sha256(value):
    res = value.encode('utf-8')
    # print(len(sha256(res).hexdigest()))
    return sha256(res).hexdigest()

"""print(hash_sha256(input('Enter a message: ')))"""

'''def hash_by_bcrypt(password):
    passw = password.encode('utf-8')
    value = bcrypt.gensalt()
    return bcrypt.hashpw(passw,value)
def check_hash_by_bcrypt(pin1,pin2):
    hash_pass = hash_by_bcrypt(pin1)
    pin = pin2.encode('utf-8')
    return bcrypt.checkpw(pin,hash_pass)

p = input('Enter a password: ')
print(f'Hash value: {hash_by_bcrypt(p)}')
print(f'Value: {check_hash_by_bcrypt(p,"Qiziqma07")}')'''

# class Hash_Table:
#     def __init__(self,size = 10):
#         self.size = size
#         self.table = [None] * size
#     def hash_func(self,key):
#         return hash_sha256(key) % self.size
#     def add(self,key,value):
#         pass
#     def remove(self,key):
#         pass
#     def get(self,key):
#         if len(self.table) == 0:
#             return -1
#         for i in self.table:
#             if self.table[]





'''class Binary_Tree:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
    def show(self):
        if self.left:
            self.left.show()
        print(self.data,end = ' : ')
        if self.right:
            self.right.show()
    def insert(self,item):
        if self.data > item:
            if self.left is None:
                self.left = Binary_Tree(item)
            else:
                self.left.insert(item)
        elif self.data < item:
            if self.right is None:
                self.right = Binary_Tree(item)
            else:
                self.right.insert(item)
        else:
            self.data = Binary_Tree(item)
    def search(self,item) -> bool:
        if self.data > item:
            if self.left:
                return self.left.search(item)
            else:
                return False
        elif self.data < item:
            if self.right:
                return self.right.search(item)
            else:
                return False
        else:
            return True
        
bt = Binary_Tree('Mojo')
bt.left = Binary_Tree('Java')
bt.right = Binary_Tree('Python')
bt.insert('C')
bt.insert('Flutter')
bt.insert('Go')
bt.insert('C++')
bt.insert('NodeJS')
bt.insert('C#')
bt.show()
print(f"\nResult: {bt.search('JS')}")'''

# arr = [36,98,54,21,75,14,24]
# print(arr)
# heapify(arr)
# print(arr)
# heappop(arr)
# print(arr)
# heappush(arr,38)
# print(arr)
# heapreplace(arr,77)
# print(arr)
# print(heappushpop(arr,95))
# print(nsmallest(3,arr))
# print(nlargest(3,arr))
def toHeap(arr,n,i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    # super formula = (i-1) // 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        toHeap(arr,n,largest)
arr = [25,36,145,74,36,365]
# print(arr)
# toHeap(arr,len(arr),len(arr) // 2 - 1)
# print(arr)
