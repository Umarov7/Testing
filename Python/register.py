import os, sys, mysql.connector as mc
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
os.system('clear')
class Registration(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Registration')
        self.setWindowIcon(QIcon('/home/ibrohim/Downloads/reg.ico'))
        self.setFixedSize(1040,520)
        self.setFont(QFont('Consolas',20))
        
        self.lb = QLabel('ID:',self)
        self.lb.setGeometry(50,30,200,50)
        self.id_txt = QLineEdit(self)
        self.id_txt.setGeometry(250,30,200,50)
        self.id_txt.setValidator(QIntValidator())
        self.id_txt.setAlignment(Qt.AlignCenter)

        self.lb1 = QLabel('Name:',self)
        self.lb1.setGeometry(50,100,200,50)
        self.nm_txt = QLineEdit(self)
        self.nm_txt.setGeometry(250,100,200,50)
        self.nm_txt.setAlignment(Qt.AlignCenter)

        self.lb2 = QLabel('Surname:',self)
        self.lb2.setGeometry(50,170,200,50)
        self.sn_txt = QLineEdit(self)
        self.sn_txt.setGeometry(250,170,200,50)
        self.sn_txt.setAlignment(Qt.AlignCenter)

        self.lb3 = QLabel('Gender:',self)
        self.lb3.setGeometry(50,240,200,50)
        self.ml = QRadioButton('Male',self)
        self.ml.setGeometry(250,240,100,50)
        self.fml = QRadioButton('Female',self)
        self.fml.setGeometry(370,240,130,50)
        
        self.lb4 = QLabel('Age:',self)
        self.lb4.setGeometry(50,310,200,50)
        self.age_txt = QSpinBox(self)
        self.age_txt.setGeometry(250,310,80,50)
        self.age_txt.setMinimum(18)
        self.age_txt.setMaximum(78)

        self.image_path = None
        self.image = QLabel(self)
        self.image.setGeometry(600,30,300,300)
        self.image.setPixmap(QPixmap('/home/ibrohim/Downloads/user.png'))

        self.image_load = QPushButton('Select avatar',self)
        self.image_load.setGeometry(625,335,250,50)
        self.image_load.clicked.connect(self.load_image)

        self.lb5 = QLabel('Email:',self)
        self.lb5.setGeometry(50,380,200,50)
        self.em_txt = QLineEdit(self)
        self.em_txt.setGeometry(250,380,200,50)
        self.em_txt.setAlignment(Qt.AlignCenter)

        self.lb6 = QLabel('Password:',self)
        self.lb6.setGeometry(50,450,200,50)
        self.pin_txt = QLineEdit(self)
        self.pin_txt.setGeometry(250,450,200,50)
        self.pin_txt.setAlignment(Qt.AlignCenter)
        self.pin_txt.setEchoMode(QLineEdit.Password)
        
        self.bn_insert = QPushButton('Insert data',self)
        self.bn_insert.setGeometry(625,420,250,50)
        self.bn_insert.clicked.connect(self.insert_info)

    def load_image(self):
        self.image_path = QFileDialog.getOpenFileName(self,'Choose an image','/home/ibrohim/Downloads')[0]
        self.image.setPixmap(QPixmap(self.image_path))
    def read_image(self):
        f = open(self.image_path,'rb')
        return f.read()
        f.close()
    def insert_info(self):
        con = mc.connect(host = 'localhost',user = 'root',password = 'root.702',database = 'Registration')
        kur = con.cursor()
        sql = f'Insert into Users(ID,Name,Surname,Gender,Age,Picture,Email,Password) Values(%s,%s,%s,%s,%s,%s,%s,%s)'
        p_id = self.id_txt.text()
        n = self.nm_txt.text()
        s = self.sn_txt.text()
        if self.ml.isChecked():
            gen = 'Male'
        else:
            gen = 'Female'
        age = self.age_txt.value()
        pic = self.read_image()
        em = self.em_txt.text()
        pw = self.pin_txt.text()

        kur.execute(sql,(int(p_id),n,s,gen,age,pic,em,pw))
        con.commit()
        print('Information successfully inserted into database')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    r = Registration()
    r.show()
    sys.exit(app.exec_())