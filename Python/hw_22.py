import os, sys, mysql.connector as mc, register
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
os.system('clear')
class Database(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db_name = None
        self.setWindowTitle('Database')
        self.setFixedSize(1040,320)
        self.setFont(QFont('Calibri',18))
        #Database
        self.lb = QLabel('Enter a name for database:',self)
        self.lb.setGeometry(50,30,400,50)
        self.db = QLineEdit(self)
        self.db.setGeometry(650,30,350,50)
        self.db.setAlignment(Qt.AlignCenter)
        self.btn = QPushButton('Create database',self)
        self.btn.setGeometry(700,90,250,50)
        self.btn.clicked.connect(self.click_db)
        #Table
        self.lb1 = QLabel('Enter a name for table:',self)
        self.lb1.setGeometry(50,160,400,50)

        self.tb = QLineEdit(self)
        self.tb.setGeometry(460,160,350,50)
        self.tb.setAlignment(Qt.AlignCenter)

        self.bn_table = QPushButton('Create table',self)
        self.bn_table.setGeometry(820,160,200,50)
        self.bn_table.clicked.connect(self.click_tb)
        #Next Window
        self.next_w = QPushButton('Insert data',self)
        self.next_w.setGeometry(0,220,1040,100)
        self.next_w.setFont(QFont('Calibri',36))
        self.next_w.clicked.connect(self.next_window)
    def click_db(self):
        print(f'Database created: {self.db.text()}')
        con = mc.connect(host = 'localhost',user = 'root',password = 'root.702')
        self.kur = con.cursor()
        self.kur.execute(f'Create database if not exists {self.db.text()}')
        self.db_name = self.db.text()
    def click_tb(self):
        if self.db_name is not None:
            con = mc.connect(host = 'localhost',user = 'root',password = 'root.702',database = f'{self.db_name}')
            self.kur = con.cursor()
            self.kur.execute(f'''Create table if not exists {self.tb.text()}(ID int,Name varchar(30),Surname varchar(30),
            Gender varchar(10),Age int,Picture blob,Email varchar(30),Password varchar(30));''')
            con.commit()
        else:
            print('Database Error')
    def next_window(self):
        self.window = register.Registration()
        self.window.show()
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    d = Database()
    d.show()
    sys.exit(app.exec_())