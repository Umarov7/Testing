import os, sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
os.system('clear')
# 1-task
'''
class Room:
    def __init__(self,l,w,h):
        self.length = l
        self.width = w
        self.height = h
    def show_size(self):
        sq = self.length * self.width
        print(f'Total area of the room: {sq}sqkm')
        print(f'Height of the room: {self.height}')
    def windows(self):
        res = (self.length * self.width * self.height) // (2 * 15)
        return f'The room would fit {res} windows\n'

ls = []
count = 0
for x in range(5):
    count += 1
    print(f'Room {count}.')
    l = int(input('Enter length(uzunligi): '))
    w = int(input('Enter width(eni): '))
    h = int(input('Enter height(bo\'yi): '))
    ls.append(Room(l,w,h))
os.system('clear')
c = 0
for y in ls:
    c += 1
    print(f'Room {c}.')
    y.show_size()
    print(y.windows())
'''
# 2-task
"""
class Product:
    def __init__(self,n,p,y):
        self.name = n
        self.price = p
        self.year = y
class License_product(Product):
    def __init__(self,n,p,y,d):
        super().__init__(n,p,y)
        self.date = d
    def find_days(self):
        y1 = int(self.year.split('.')[2])
        y2 = int(self.date.split('.')[2])
        m1 = int(self.year.split('.')[1])
        m2 = int(self.date.split('.')[1])
        d1 = int(self.year.split('.')[0])
        d2 = int(self.date.split('.')[0])
        y_res = (y2 - y1) * 365
        m_res = (m2 - m1) * 30
        d_res = d2 - d1
        if y_res == 0 and m_res == 0 and d_res == 0:
            return 0
        if y_res == 0:
            if m_res == 0:
                return d2 - d1
            else:
                res = 30 - d1
                for x in range(m1+1,m2):
                    res += 30
                res += d2
                return res
        else:
            res = 365 - (m1 * 30) - (30 - d1)
            for x in range(y1+1,y2):
                res += 365
            res += 365 - (m2 * 30) - (30 - d2)
            return res

ls = []
count = 0
for x in range(5):
    count += 1
    print(f'Product {count}.')
    n = input('Enter name: ')
    p = int(input('Enter price: '))
    y = input('Enter the made year: ')
    d = input('Enter the arrival date at the shop: ')
    ls.append(License_product(n,p,y,d))
os.system('clear')
c = 0
for y in ls:
    c += 1
    print(f'Product {c}.')
    print(f'It took {y.name} {y.find_days()} days to arrive at the shop')
"""
# 3-task
class Project(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Prime numbers')
        self.setFixedSize(1000,500)
        self.setFont(QFont('',20))

        self.ln = QLineEdit(self)
        self.ln.setGeometry(400,50,200,50)

        self.bn = QPushButton('Display',self)
        self.bn.setGeometry(425,150,150,50)
        self.bn.setStyleSheet('background: lime')
        self.bn.clicked.connect(self.show_prime)

        self.inp = QLabel('INPUT',self)
        self.inp.setGeometry(450,250,100,50)
        self.inp.setStyleSheet('border: 2px solid red')
        self.inp.setAlignment(Qt.AlignCenter)

        self.out = QLabel('OUTPUT',self)
        self.out.setGeometry(100,350,800,50)
        self.out.setStyleSheet('border: 3px solid blue')
        self.out.setAlignment(Qt.AlignCenter)

    def isPrime(self,x):
        i = 2
        while i * i <= x:
            if x % i == 0:
                return False
            i += 1
        return True
    def show_prime(self):
        n = int(self.ln.text())
        self.inp.setText(self.ln.text())
        ls = []
        for x in range(2,n):
            if self.isPrime(x) == True:
                ls.append(x)
        self.out.setText(str(ls))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    p = Project()
    p.show()
    sys.exit(app.exec_())