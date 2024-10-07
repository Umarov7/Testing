import os,sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
os.system('clear')

# 1-task
"""
class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tests')
        self.setWindowIcon(QIcon('/home/ibrohim/Downloads/icon_test.ico'))
        self.setFixedSize(900,550)

        self.t1 = QLabel('He studies in __ London',self)
        self.t1.setGeometry(20,20,328,40)
        self.t1.setFont(QFont('',20))
        self.t1.setStyleSheet('''border-color: green;
        border-width: 3px;
        border-style: solid;''')
        
        self.rb1_one = QRadioButton('a/an',self)
        self.rb1_one.setFont(QFont('Consolas',18))
        self.rb1_one.move(400,25)
        self.rb2_one = QRadioButton('the',self)
        self.rb2_one.setFont(QFont('Consolas',18))
        self.rb2_one.move(550,25)
        self.rb3_one = QRadioButton('−',self)
        self.rb3_one.move(700,25)
        self.rb3_one.setFont(QFont('Consolas',18))
        self.rb_g_one = QButtonGroup(self)
        self.rb_g_one.addButton(self.rb1_one)
        self.rb_g_one.addButton(self.rb2_one)
        self.rb_g_one.addButton(self.rb3_one)


        self.t2 = QLabel('Do you __ in a house?',self)
        self.t2.setGeometry(20,100,328,40)
        self.t2.setFont(QFont('',20))
        self.t2.setStyleSheet('''border-color: red;
        border-width: 3px;
        border-style: solid;''')
        
        self.rb1_two = QRadioButton('live',self)
        self.rb1_two.setFont(QFont('Consolas',18))
        self.rb1_two.move(400,105)
        self.rb2_two = QRadioButton('lives',self)
        self.rb2_two.setFont(QFont('Consolas',18))
        self.rb2_two.move(550,105)
        self.rb3_two = QRadioButton('lived',self)
        self.rb3_two.move(700,105)
        self.rb3_two.setFont(QFont('Consolas',18))
        self.rb_g_two = QButtonGroup(self)
        self.rb_g_two.addButton(self.rb1_two)
        self.rb_g_two.addButton(self.rb2_two)
        self.rb_g_two.addButton(self.rb3_two)


        self.t3 = QLabel('She __ a film yesterday',self)
        self.t3.setGeometry(20,180,328,40)
        self.t3.setFont(QFont('',20))
        self.t3.setStyleSheet('''border-color: blue;
        border-width: 3px;
        border-style: solid;''')
        
        self.rb1_three = QRadioButton('watch',self)
        self.rb1_three.setFont(QFont('Consolas',18))
        self.rb1_three.move(400,185)
        self.rb2_three = QRadioButton('watched',self)
        self.rb2_three.setFont(QFont('Consolas',18))
        self.rb2_three.move(550,185)
        self.rb2_three.resize(160,30)
        self.rb3_three = QRadioButton('watching',self)
        self.rb3_three.move(700,185)
        self.rb3_three.setFont(QFont('Consolas',18))
        self.rb3_three.resize(160,30)
        self.rb_g_three = QButtonGroup(self)
        self.rb_g_three.addButton(self.rb1_three)
        self.rb_g_three.addButton(self.rb2_three)
        self.rb_g_three.addButton(self.rb3_three)


        self.t4 = QLabel('Who are they __ to?',self)
        self.t4.setGeometry(20,260,328,40)
        self.t4.setFont(QFont('',20))
        self.t4.setStyleSheet('''border-color: yellow;
        border-width: 3px;
        border-style: solid;''')
        
        self.rb1_four = QRadioButton('talk',self)
        self.rb1_four.setFont(QFont('Consolas',18))
        self.rb1_four.move(400,265)
        self.rb2_four = QRadioButton('talks',self)
        self.rb2_four.setFont(QFont('Consolas',18))
        self.rb2_four.move(550,265)
        self.rb2_four.resize(160,30)
        self.rb3_four = QRadioButton('talking',self)
        self.rb3_four.move(700,265)
        self.rb3_four.setFont(QFont('Consolas',18))
        self.rb3_four.resize(160,30)
        self.rb_g_four = QButtonGroup(self)
        self.rb_g_four.addButton(self.rb1_four)
        self.rb_g_four.addButton(self.rb2_four)
        self.rb_g_four.addButton(self.rb3_four)


        self.t5 = QLabel('I have __ my homework',self)
        self.t5.setGeometry(20,340,328,40)
        self.t5.setFont(QFont('',20))
        self.t5.setStyleSheet('''border-color: purple;
        border-width: 3px;
        border-style: solid;''')
        
        self.rb1_five = QRadioButton('finished',self)
        self.rb1_five.setFont(QFont('Consolas',18))
        self.rb1_five.move(400,345)
        self.rb1_five.resize(160,30)
        self.rb2_five = QRadioButton('finishes',self)
        self.rb2_five.setFont(QFont('Consolas',18))
        self.rb2_five.move(550,345)
        self.rb2_five.resize(160,30)
        self.rb3_five = QRadioButton('finishing',self)
        self.rb3_five.move(700,345)
        self.rb3_five.resize(160,30)
        self.rb3_five.setFont(QFont('Consolas',18))
        self.rb_g_five = QButtonGroup(self)
        self.rb_g_five.addButton(self.rb1_five)
        self.rb_g_five.addButton(self.rb2_five)
        self.rb_g_five.addButton(self.rb3_five)

        self.btn = QPushButton('Submit',self)
        self.btn.setGeometry(375,450,150,50)
        self.btn.setFont(QFont('DejaVu Serif',26))
        self.btn.setStyleSheet('background:  #48c9b0')
        self.btn.clicked.connect(self.click_sbm)
    
    def click_sbm(self):
        p = 0
        if self.rb3_one.isChecked():
            p += 1
        if self.rb1_two.isChecked():
            p += 1
        if self.rb2_three.isChecked():
            p += 1
        if self.rb3_four.isChecked():
            p += 1
        if self.rb1_five.isChecked():
            p += 1
        msg = QMessageBox(self)
        msg.setWindowTitle('RESULTS')
        msg.setIcon(QMessageBox.Question)
        msg.setText(f'You\'ve got {p} right!\nWould you like to exit?')
        msg.setFont(QFont('',18))
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.buttonClicked.connect(self.message)
        msg.show()
    def message(self,x):
        if x.text() == '&Yes':
            exit()
        else:
            print('The programme has not been finished')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    t = Test()
    t.show()
    sys.exit(app.exec_())
"""
# 2-task
'''
class Restaurant(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1200,800)
        self.setFont(QFont('',20))
        self.setWindowTitle('Menu')
        self.setWindowIcon(QIcon('/home/ibrohim/Downloads/icon_menu.ico'))

        self.starter = QLabel('Starters',self)
        self.starter.setGeometry(50,50,200,50)
        self.starter.setFont(QFont('DejaVu Serif',22))
        self.st_1 = QCheckBox('Soup',self)
        self.st_1.setGeometry(50,100,100,50)
        self.st_2 = QCheckBox('Salad',self)
        self.st_2.setGeometry(50,150,100,50)

        self.main = QLabel('Main courses',self)
        self.main.setGeometry(350,50,200,50)
        self.main.setFont(QFont('DejaVu Serif',22))
        self.m_1 = QCheckBox('Grilled Chicken',self)
        self.m_1.setGeometry(350,100,220,50)
        self.m_2 = QCheckBox('Seafood',self)
        self.m_2.setGeometry(350,150,200,50)

        self.dessert = QLabel('Desserts',self)
        self.dessert.setGeometry(700,50,200,50)
        self.dessert.setFont(QFont('DejaVu Serif',22))
        self.d_1 = QCheckBox('Apple Pie',self)
        self.d_1.setGeometry(700,100,220,50)
        self.d_2 = QCheckBox('Fruit Salad',self)
        self.d_2.setGeometry(700,150,200,50)

        self.drinks = QLabel('Drinks',self)
        self.drinks.setGeometry(1000,50,200,50)
        self.drinks.setFont(QFont('DejaVu Serif',22))
        self.dr_1 = QCheckBox('Tea',self)
        self.dr_1.setGeometry(1000,100,150,50)
        self.dr_2 = QCheckBox('Coffee',self)
        self.dr_2.setGeometry(1000,150,150,50)

        self.bn = QPushButton(self)
        self.bn.setText('Bill')
        self.bn.move(550,250)
        self.bn.resize(100,50)
        self.bn.clicked.connect(self.show_bill)

        self.t = QTextEdit(self)
        self.t.setGeometry(300,400,600,300)
        self.t.setStyleSheet('border: 2px solid black;')
    
    def show_bill(self):
        b,txt = 0,''
        if self.st_1.isChecked():
            b += 6
            txt += f'{self.st_1.text()}: 6$\n'
        if self.st_2.isChecked():
            b += 5
            txt += f'{self.st_2.text()}: 5$\n'
        if self.m_1.isChecked():
            b += 10
            txt += f'{self.m_1.text()}: 10$\n'
        if self.m_2.isChecked():
            b += 11
            txt += f'{self.m_2.text()}: 11$\n'
        if self.d_1.isChecked():
            b += 6
            txt += f'{self.d_1.text()}: 6$\n'
        if self.d_2.isChecked():
            b += 4
            txt += f'{self.d_2.text()}: 4$\n'
        if self.dr_1.isChecked():
            b += 2
            txt += f'{self.dr_1.text()}: 2$\n'
        if self.dr_2.isChecked():
            b += 3
            txt += f'{self.dr_2.text()}: 3$\n'
        txt += f'Total bill: {b}$'
        self.t.setText(txt)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    r = Restaurant()
    r.show()
    sys.exit(app.exec_())
'''
# 3-task
class Information(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFont(QFont('Calibri',20))
        self.setFixedSize(1800,500)

        self.city = QComboBox(self)
        self.city.setGeometry(40,50,400,50)
        self.city.setStyleSheet('background: green;')
        self.city.addItems(['Tashkent','Bukhara','Samarkand','Khiva'])

        self.district = QComboBox(self)
        self.district.setGeometry(480,50,400,50)
        self.district.setStyleSheet('background: red;')
        self.district.addItems(['Yunusabad','Chilanzar','Almazar','Sergeli'])

        self.nationality = QComboBox(self)
        self.nationality.setGeometry(920,50,400,50)
        self.nationality.setStyleSheet('background: blue;')
        self.nationality.addItems(['Uzbek','Tajik','Kazakh','Kyrgyz'])

        self.gender = QComboBox(self)
        self.gender.setGeometry(1360,50,400,50)
        self.gender.setStyleSheet('background: yellow;')
        self.gender.addItems(['Male','Female'])

        self.bn = QPushButton(self)
        self.bn.setText('Display')
        self.bn.move(750,225)
        self.bn.resize(300,50)
        self.bn.setStyleSheet('background: #7D3C98')
        self.bn.clicked.connect(self.show_info)
    
    def show_info(self):
        info = f'{self.gender.currentText()} {self.nationality.currentText()} lives in {self.district.currentText()}, {self.city.currentText()}'
        msg = QMessageBox(self)
        msg.setText(info)
        msg.setWindowTitle('INFO')
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.buttonClicked.connect(self.message)
        msg.show()
    def message(self,x):
        if x.text() == '&Yes':
            exit()
        else:
            print('The programme has not been finished')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    i = Information()
    i.show()
    sys.exit(app.exec_())