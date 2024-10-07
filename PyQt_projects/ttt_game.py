import os, sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
os.system('clear')
class TicTacToe(QMainWindow):
    __count = 0
    def __init__(self):
        super().__init__()
        self.setWindowTitle('TIC TAC TOE')
        self.setWindowIcon(QIcon('/home/ibrohim/Downloads/icon_tic-tac-toe.ico'))
        self.setFixedSize(900,600)
        self.setFont(QFont('',90))

        self.btn1 = self.button_maker('',self)
        self.btn1.move(50,50)
        self.btn2 = self.button_maker('',self)
        self.btn2.move(200,50)
        self.btn3 = self.button_maker('',self)
        self.btn3.move(350,50)
        self.btn4 = self.button_maker('',self)
        self.btn4.move(50,200)
        self.btn5 = self.button_maker('',self)
        self.btn5.move(200,200)
        self.btn6 = self.button_maker('',self)
        self.btn6.move(350,200)
        self.btn7 = self.button_maker('',self)
        self.btn7.move(50,350)
        self.btn8 = self.button_maker('',self)
        self.btn8.move(200,350)
        self.btn9 = self.button_maker('',self)
        self.btn9.move(350,350)

        self.__ls_btn = [self.btn1,self.btn2,self.btn3,self.btn4,self.btn5,self.btn6,self.btn7,self.btn8,self.btn9]
        self.functions = [self.btn1_click,self.btn2_click,self.btn3_click,self.btn4_click,self.btn5_click,self.btn6_click,
        self.btn7_click,self.btn8_click,self.btn9_click]
        for x,y in zip(self.__ls_btn,self.functions):
            x.clicked.connect(y)
        
        self.new_game = QPushButton('New Game',self)
        self.new_game.setGeometry(600,250,200,50)
        self.new_game.setFont(QFont('Calibri',22))
        self.new_game.setStyleSheet('color: white; background: black;')
        self.new_game.clicked.connect(self.start_game)
        
    def button_maker(self,x,y):
        btn = QPushButton(x,y)
        btn.resize(150,150)
        btn.setStyleSheet('''color: lime;
        border: 2px solid white;
        background-color: black;''')
        return btn

    def start_game(self):
        TicTacToe.__count = 0
        for i in self.__ls_btn:
            i.setText('')
            i.setEnabled(True)
    
    def check_game(self):
        combinations = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for j in combinations:
            if self.__ls_btn[j[0]].text() == self.__ls_btn[j[1]].text() == self.__ls_btn[j[2]].text() != '':
                winner = self.__ls_btn[j[0]].text()
                QMessageBox.information(self, 'Game Over', f'Player {winner} wins!')
                self.start_game()
                return
        if all(k.text() for k in self.__ls_btn):
            QMessageBox.information(self, 'Game Over', 'It\'s a tie!')
            self.start_game()
            return

    def btn1_click(self):
        TicTacToe.__count += 1
        if TicTacToe.__count % 2 != 0:
            self.btn1.setText('X')
        else:
            self.btn1.setText('O')
        self.btn1.setEnabled(False)
        self.check_game()
    def btn2_click(self):
        TicTacToe.__count += 1
        if TicTacToe.__count % 2 != 0:
            self.btn2.setText('X')
        else:
            self.btn2.setText('O')
        self.btn2.setEnabled(False)
        self.check_game()
    def btn3_click(self):
        TicTacToe.__count += 1
        if TicTacToe.__count % 2 != 0:
            self.btn3.setText('X')
        else:
            self.btn3.setText('O')
        self.btn3.setEnabled(False)
        self.check_game()
    def btn4_click(self):
        TicTacToe.__count += 1
        if TicTacToe.__count % 2 != 0:
            self.btn4.setText('X')
        else:
            self.btn4.setText('O')
        self.btn4.setEnabled(False)
        self.check_game()
    def btn5_click(self):
        TicTacToe.__count += 1
        if TicTacToe.__count % 2 != 0:
            self.btn5.setText('X')
        else:
            self.btn5.setText('O')
        self.btn5.setEnabled(False)
        self.check_game()
    def btn6_click(self):
        TicTacToe.__count += 1
        if TicTacToe.__count % 2 != 0:
            self.btn6.setText('X')
        else:
            self.btn6.setText('O')
        self.btn6.setEnabled(False)
        self.check_game()
    def btn7_click(self):
        TicTacToe.__count += 1
        if TicTacToe.__count % 2 != 0:
            self.btn7.setText('X')
        else:
            self.btn7.setText('O')
        self.btn7.setEnabled(False)
        self.check_game()
    def btn8_click(self):
        TicTacToe.__count += 1
        if TicTacToe.__count % 2 != 0:
            self.btn8.setText('X')
        else:
            self.btn8.setText('O')
        self.btn8.setEnabled(False)
        self.check_game()
    def btn9_click(self):
        TicTacToe.__count += 1
        if TicTacToe.__count % 2 != 0:
            self.btn9.setText('X')
        else:
            self.btn9.setText('O')
        self.btn9.setEnabled(False)
        self.check_game()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    t = TicTacToe()
    t.show()
    sys.exit(app.exec_())