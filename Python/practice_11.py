import os, sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
os.system('clear')

class Survey(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Survey')
        self.setFixedSize(500,550)
        self.setFont(QFont('',18))

        self.lb_name = QLabel('Name:',self)
        self.lb_name.setGeometry(10,10,100,50)
        self.ln_name = QLineEdit('',self)
        self.ln_name.setGeometry(190,20,300,30)
        self.ln_name.setStyleSheet('border: 2px solid black')

        self.lb_sur = QLabel('Surname:',self)
        self.lb_sur.setGeometry(10,60,100,50)
        self.ln_sur = QLineEdit('',self)
        self.ln_sur.setGeometry(190,70,300,30)
        self.ln_sur.setStyleSheet('border: 2px solid black')

        self.lb_age = QLabel('Age:',self)
        self.lb_age.setGeometry(10,110,100,50)
        self.sb_age = QSpinBox(self)
        self.sb_age.setValue(0)
        self.sb_age.setGeometry(190,118,300,35)

        self.lb_gen = QLabel('Gender:',self)
        self.lb_gen.setGeometry(10,160,100,50)
        self.rb1_gen = QRadioButton('Male',self)
        self.rb1_gen.setGeometry(190,160,100,50)
        self.rb2_gen = QRadioButton('Female',self)
        self.rb2_gen.setGeometry(190,200,100,50)

        self.lb_add = QLabel('Address:',self)
        self.lb_add.setGeometry(10,240,100,50)
        self.cb_add = QComboBox(self)
        self.cb_add.setGeometry(190,245,300,35)
        self.cb_add.addItems(['Tashkent','Bukhara','Samarkand','Khiva'])

        self.lb_phn = QLabel('Phone number:',self)
        self.lb_phn.setGeometry(10,290,170,50)
        self.ln_phn = QLineEdit('',self)
        self.ln_phn.setGeometry(190,300,300,30)
        self.ln_phn.setStyleSheet('border: 2px solid black')

        self.lb_fac = QLabel('Faculty:',self)
        self.lb_fac.setGeometry(10,340,170,50)
        self.ln_fac = QLineEdit('',self)
        self.ln_fac.setGeometry(190,350,300,30)
        self.ln_fac.setStyleSheet('border: 2px solid black')

        self.lb_cou = QLabel('Course:',self)
        self.lb_cou.setGeometry(10,390,100,50)
        self.cb_cou = QComboBox(self)
        self.cb_cou.setGeometry(190,400,300,35)
        self.cb_cou.addItems(['1','2','3','4'])

        self.lb_con = QLabel('Confirmation:',self)
        self.lb_con.setGeometry(10,440,150,50)
        self.chb_con = QCheckBox('Confirm',self)
        self.chb_con.setGeometry(190,440,125,50)

        self.bn = QPushButton('Save',self)
        self.bn.setGeometry(10,490,480,50)
        self.bn.clicked.connect(self.click_bn)
    
    def click_bn(self):
        f = open('/home/ibrohim/Downloads/Student.txt','w+')
        txt = ''
        txt += f'Full name: {self.ln_name.text()} {self.ln_sur.text()}\n'
        txt += f'Age: {self.sb_age.value()}\n'
        if self.rb1_gen.isChecked():
            txt += f'Gender: {self.rb1_gen.text()}\n'
        else:
            txt += f'Gender: {self.rb2_gen.text()}\n'
        txt += f'Address: {self.cb_add.currentText()}\n'
        txt += f'Phone number: {self.ln_phn.text()}\n'
        txt += f'Faculty: {self.ln_fac.text()}\n'
        txt += f'Course: {self.cb_cou.currentText()}\n'
        if self.chb_con.isChecked():
            txt += 'Status: Confirmed\n'
        else:
            txt += 'Status: Unconfirmed\n'
        f.write(txt)
        f.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    s = Survey()
    s.show()
    sys.exit(app.exec_())