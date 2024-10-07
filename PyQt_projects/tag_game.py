import os, sys, random
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Game(QMainWindow):
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
    sys.exit(app.exec_())