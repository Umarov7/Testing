import os,sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
os.system("clear")

class Calculator(QMainWindow):
    __operator = None
    __n1 = None
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("/home/ibrohim/Downloads/icon_calculator.ico"))
        self.setFixedSize(420,850)
        self.setStyleSheet("""
        background-color: rgb(0,0,0);
        border-style: solid;
        border-width: 3px;
        border-color: rgb(253,254,254);
        border-radius: 25px;""")

        self.ln = QPushButton(self)
        self.ln.setGeometry(130,820,150,5)
        self.ln.setStyleSheet('''background-color: rgb(253, 254, 254);''')

        self.calculation = QLabel('0',self)
        self.calculation.setGeometry(20,220,380,80)
        self.calculation.setFont(QFont('Calibri Light',50))
        self.calculation.setStyleSheet('color: white; border: black;')
        self.calculation.setAlignment(Qt.AlignRight)
        
        self.bn_ac = QPushButton("AC",self)
        self.bn_ac.setGeometry(30,320,75,75)
        self.bn_ac.setFont(QFont("Poor Richard",22))
        self.bn_ac.setStyleSheet("""
        background-color: rgb(202, 207, 210);
        border-style: solid;
        border-width: 3px;
        border-color: rgb(202, 207, 210);
        border-radius: 35px;""")
        self.bn_ac.clicked.connect(self.click_ac)

        self.bn_pdm = QPushButton("+/-",self)
        self.bn_pdm.setGeometry(125,320,75,75)
        self.bn_pdm.setFont(QFont("Poor Richard",22))
        self.bn_pdm.setStyleSheet("""
        background-color: rgb(202, 207, 210);
        border-style: solid;
        border-width: 3px;
        border-color: rgb(202, 207, 210);
        border-radius: 35px;""")
        self.bn_pdm.clicked.connect(self.click_pdm)

        self.bn_per = QPushButton("%",self)
        self.bn_per.setGeometry(220,320,75,75)
        self.bn_per.setFont(QFont("Poor Richard",22))
        self.bn_per.setStyleSheet("""
        background-color: rgb(202, 207, 210);
        border-style: solid;
        border-width: 3px;
        border-color: rgb(202, 207, 210);
        border-radius: 35px;""")
        self.bn_per.clicked.connect(self.click_per)

        self.bn_div = QPushButton("÷",self)
        self.bn_div.setGeometry(315,320,75,75)
        self.bn_div.setFont(QFont("Poor Richard",30))
        self.bn_div.setStyleSheet("""
        background-color: rgb(243, 156, 18);
        border-style: solid;
        border-width: 3px;
        border-color: rgb(243, 156, 18);
        border-radius: 35px;
        color: rgb(253,254,254);""")
        self.bn_div.clicked.connect(self.click_div)


        self.bn_7 = QPushButton("7",self)
        self.bn_7.setGeometry(30,415,75,75)
        self.bn_7.setFont(QFont("Poor Richard",22))
        self.bn_7.setStyleSheet("""
        background-color: rgb(98, 101, 103);
        border-style: solid;
        border-width: 3px;
        border-color: rgb(98, 101, 103);
        border-radius: 35px;
        color: rgb(253,254,254);""")
        self.bn_7.clicked.connect(self.click_7)

        self.bn_8 = QPushButton("8",self)
        self.bn_8.setGeometry(125,415,75,75)
        self.bn_8.setFont(QFont("Poor Richard",22))
        self.bn_8.setStyleSheet("""
        background-color: rgb(98, 101, 103);
        border-style: solid;
        border-width: 3px;
        border-color: rgb(98, 101, 103);
        border-radius: 35px;
        color: rgb(253,254,254);""")
        self.bn_8.clicked.connect(self.click_8)

        self.bn_9 = QPushButton("9",self)
        self.bn_9.setGeometry(220,415,75,75)
        self.bn_9.setFont(QFont("Poor Richard",22))
        self.bn_9.setStyleSheet("""
        background-color: rgb(98, 101, 103);
        border-style: solid;
        border-width: 3px;
        border-color: rgb(98, 101, 103);
        border-radius: 35px;
        color: rgb(253,254,254);""")
        self.bn_9.clicked.connect(self.click_9)

        self.bn_mul = QPushButton("×",self)
        self.bn_mul.setGeometry(315,415,75,75)
        self.bn_mul.setFont(QFont("Poor Richard",28))
        self.bn_mul.setStyleSheet("""
        background-color: rgb(243, 156, 18);
        border-style: solid;
        border-width: 3px;
        border-color: rgb(243, 156, 18);
        border-radius: 35px;
        color: rgb(253,254,254);""")
        self.bn_mul.clicked.connect(self.click_mul)


        self.bn_4 = QPushButton("4",self)
        self.bn_4.setGeometry(30,510,75,75)
        self.bn_4.setFont(QFont("Poor Richard",22))
        self.bn_4.setStyleSheet("""
        background-color: rgb(98, 101, 103);
        border-style: solid;
        border-width: 3px;
        border-color: rgb(98, 101, 103);
        border-radius: 35px;
        color: rgb(253,254,254);""")
        self.bn_4.clicked.connect(self.click_4)

        self.bn_5 = QPushButton("5",self)
        self.bn_5.setGeometry(125,510,75,75)
        self.bn_5.setFont(QFont("Poor Richard",22))
        self.bn_5.setStyleSheet("""
        background-color: rgb(98, 101, 103);
        border-style: solid;
        border-width: 3px;
        border-color: rgb(98, 101, 103);
        border-radius: 35px;
        color: rgb(253,254,254);""")
        self.bn_5.clicked.connect(self.click_5)

        self.bn_6 = QPushButton("6",self)
        self.bn_6.setGeometry(220,510,75,75)
        self.bn_6.setFont(QFont("Poor Richard",22))
        self.bn_6.setStyleSheet("""
        background-color: rgb(98, 101, 103);
        border-style: solid;
        border-width: 3px;
        border-color: rgb(98, 101, 103);
        border-radius: 35px;
        color: rgb(253,254,254);""")
        self.bn_6.clicked.connect(self.click_6)

        self.bn_min = QPushButton("−",self)
        self.bn_min.setGeometry(315,510,75,75)
        self.bn_min.setFont(QFont("Poor Richard",26))
        self.bn_min.setStyleSheet("""
        background-color: rgb(243, 156, 18);
        border-style: solid;
        border-width: 3px;
        border-color: rgb(243, 156, 18);
        border-radius: 35px;
        color: rgb(253,254,254);""")
        self.bn_min.clicked.connect(self.click_min)


        self.bn_1 = QPushButton("1",self)
        self.bn_1.setGeometry(30,605,75,75)
        self.bn_1.setFont(QFont("Poor Richard",22))
        self.bn_1.setStyleSheet("""
        background-color: rgb(98, 101, 103);
        border-style: solid;
        border-width: 3px;
        border-color: rgb(98, 101, 103);
        border-radius: 35px;
        color: rgb(253,254,254);""")
        self.bn_1.clicked.connect(self.click_1)

        self.bn_2 = QPushButton("2",self)
        self.bn_2.setGeometry(125,605,75,75)
        self.bn_2.setFont(QFont("Poor Richard",22))
        self.bn_2.setStyleSheet("""
        background-color: rgb(98, 101, 103);
        border-style: solid;
        border-width: 3px;
        border-color: rgb(98, 101, 103);
        border-radius: 35px;
        color: rgb(253,254,254);""")
        self.bn_2.clicked.connect(self.click_2)

        self.bn_3 = QPushButton("3",self)
        self.bn_3.setGeometry(220,605,75,75)
        self.bn_3.setFont(QFont("Poor Richard",22))
        self.bn_3.setStyleSheet("""
        background-color: rgb(98, 101, 103);
        border-style: solid;
        border-width: 3px;
        border-color: rgb(98, 101, 103);
        border-radius: 35px;
        color: rgb(253,254,254);""")
        self.bn_3.clicked.connect(self.click_3)

        self.bn_pl = QPushButton("+",self)
        self.bn_pl.setGeometry(315,605,75,75)
        self.bn_pl.setFont(QFont("Poor Richard",28))
        self.bn_pl.setStyleSheet("""
        background-color: rgb(243, 156, 18);
        border-style: solid;
        border-width: 3px;
        border-color: rgb(243, 156, 18);
        border-radius: 35px;
        color: rgb(253,254,254);""")
        self.bn_pl.clicked.connect(self.click_pl)


        self.bn_0 = QPushButton("0",self)
        self.bn_0.setGeometry(30,700,170,75)
        self.bn_0.setFont(QFont("Poor Richard",22))
        self.bn_0.setStyleSheet("""
        text-align: left;
        background-color: rgb(98, 101, 103);
        border-style: solid;
        border-width: 3px;
        border-color: rgb(98, 101, 103);
        border-radius: 35px;
        color: rgb(253,254,254);""")
        self.bn_0.clicked.connect(self.click_0)

        self.bn_d = QPushButton(".",self)
        self.bn_d.setGeometry(220,700,75,75)
        self.bn_d.setFont(QFont("Poor Richard",32))
        self.bn_d.setStyleSheet("""
        background-color: rgb(98, 101, 103);
        border-style: solid;
        border-width: 3px;
        border-color: rgb(98, 101, 103);
        border-radius: 35px;
        color: rgb(253,254,254);""")
        self.bn_d.clicked.connect(self.click_d)

        self.bn_eq = QPushButton("=",self)
        self.bn_eq.setGeometry(315,700,75,75)
        self.bn_eq.setFont(QFont("Poor Richard",26))
        self.bn_eq.setStyleSheet("""
        background-color: rgb(243, 156, 18);
        border-style: solid;
        border-width: 3px;
        border-color: rgb(243, 156, 18);
        border-radius: 35px;
        color: rgb(253,254,254);""")
        self.bn_eq.clicked.connect(self.click_eq)

    def click_ac(self):
        self.calculation.setText('0')
    def click_pdm(self):
        pass
    def click_per(self):
        Calculator.__operator = '%'
        Calculator.__n1 = int(self.calculation.text())
        self.calculation.setText('0')
    def click_div(self):
        Calculator.__operator = '/'
        Calculator.__n1 = int(self.calculation.text())
        self.calculation.setText('0')
    
    
    def click_7(self):
        n = self.calculation.text()
        if n == '0':
            n = '7'
        else:
            n += '7'
        self.calculation.setText(n)
    def click_8(self):
        n = self.calculation.text()
        if n == '0':
            n = '8'
        else:
            n += '8'
        self.calculation.setText(n)
    def click_9(self):
        n = self.calculation.text()
        if n == '0':
            n = '9'
        else:
            n += '9'
        self.calculation.setText(n)
    def click_mul(self):
        Calculator.__operator = '*'
        Calculator.__n1 = int(self.calculation.text())
        self.calculation.setText('0')
    

    def click_4(self):
        n = self.calculation.text()
        if n == '0':
            n = '4'
        else:
            n += '4'
        self.calculation.setText(n)
    def click_5(self):
        n = self.calculation.text()
        if n == '0':
            n = '5'
        else:
            n += '5'
        self.calculation.setText(n)
    def click_6(self):
        n = self.calculation.text()
        if n == '0':
            n = '6'
        else:
            n += '6'
        self.calculation.setText(n)
    def click_min(self):
        Calculator.__operator = '-'
        Calculator.__n1 = int(self.calculation.text())
        self.calculation.setText('0')
    

    def click_1(self):
        n = self.calculation.text()
        if n == '0':
            n = '1'
        else:
            n += '1'
        self.calculation.setText(n)
    def click_2(self):
        n = self.calculation.text()
        if n == '0':
            n = '2'
        else:
            n += '2'
        self.calculation.setText(n)
    def click_3(self):
        n = self.calculation.text()
        if n == '0':
            n = '3'
        else:
            n += '3'
        self.calculation.setText(n)
    def click_pl(self):
        Calculator.__operator = '+'
        Calculator.__n1 = int(self.calculation.text())
        self.calculation.setText('0')
    

    def click_0(self):
        n = self.calculation.text()
        if n == '0':
            n = '0'
        else:
            n += '0'
        self.calculation.setText(n)
    def click_d(self):
        n = self.calculation.text()
        if n != '0' and not '.' in n:
            n += '.'
        self.calculation.setText(n)
    def click_eq(self):
        n2 = int(self.calculation.text())
        match Calculator.__operator:
            case '+':
                self.calculation.setText(str(Calculator.__n1 + n2))
            case '-':
                self.calculation.setText(str(Calculator.__n1 - n2))
            case '*':
                self.calculation.setText(str(Calculator.__n1 * n2))
            case '/':
                self.calculation.setText(str(Calculator.__n1 / n2))
            case '%':
                self.calculation.setText(str(Calculator.__n1 % n2))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    cl = Calculator()
    cl.show()
    sys.exit(app.exec_())
