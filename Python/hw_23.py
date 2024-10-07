import os, sys, mysql.connector as mc
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
os.system('clear')
class Telephone(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tech database')
        self.setWindowIcon(QIcon('/home/ibrohim/Downloads/phone.ico'))
        self.setFixedSize(1820,1000)
        self.setStyleSheet('color: rgb(0,0,205); background-color: rgb(230,230,250)')
        self.my_con = None
        self.my_cur = None
        self.tb = QTableWidget(self)
        self.tb.setFont(QFont('Poor Richard',20))
        self.tb.setVisible(False)
        self.next = New_window()
        #Model
        self.lb_model = QLabel('Model:',self)
        self.lb_model.setGeometry(50,30,250,50)
        self.lb_model.setFont(QFont('Consolas',20))
        self.txt_model = QLineEdit(self)
        self.txt_model.setGeometry(310,30,300,50)
        self.txt_model.setFont(QFont('Consolas',20))
        self.txt_model.setAlignment(Qt.AlignRight)
        self.txt_model.setStyleSheet('''border: 2px inset rgb(0,27,254); border-radius: 25px;''')
        #Price
        self.lb_price = QLabel('Price:',self)
        self.lb_price.setGeometry(1000,30,250,50)
        self.lb_price.setFont(QFont('Consolas',20))
        self.txt_price = QLineEdit(self)
        self.txt_price.setGeometry(1260,30,300,50)
        self.txt_price.setFont(QFont('Consolas',20))
        self.txt_price.setAlignment(Qt.AlignRight)
        self.txt_price.setValidator(QIntValidator())
        self.txt_price.setStyleSheet('''border: 2px inset rgb(0,27,254); border-radius: 25px;''')
        #E_SIM
        self.lb_esim = QLabel('Select:',self)
        self.lb_esim.setGeometry(50,90,250,50)
        self.lb_esim.setFont(QFont('Consolas',20))
        self.txt_esim = QCheckBox('ESIM',self)
        self.txt_esim.setGeometry(510,90,100,50)
        self.txt_esim.setFont(QFont('Consolas',20))
        #Colour
        self.lb_colour = QLabel('Colour:',self)
        self.lb_colour.setGeometry(1000,90,250,50)
        self.lb_colour.setFont(QFont('Consolas',20))
        self.txt_colour = QComboBox(self)
        self.txt_colour.setGeometry(1260,90,300,50)
        self.txt_colour.setFont(QFont('Consolas',20))
        self.txt_colour.setStyleSheet('''border: 2px inset rgb(0,27,254); border-radius: 15px;''')
        self.txt_colour.addItems(['Red','Blue','Black','White','Green','Yellow','Magenta','Gold','Silver'])
        #Button
        self.insert_btn = QPushButton('Insert info',self)
        self.insert_btn.setGeometry(1500,145,300,50)
        self.insert_btn.setFont(QFont('Consolas',20))
        self.insert_btn.setStyleSheet('''background: black; color:rgb(0,255,0); border: 2px outset rgb(0,255,0); border-radius: 15px;''')
        self.insert_btn.clicked.connect(self.insert_data)
        #Column
        self.lb_column = QLabel('Select column:',self)
        self.lb_column.setGeometry(50,300,250,50)
        self.lb_column.setFont(QFont('Consolas',20))
        self.txt_column = QComboBox(self)
        self.txt_column.setGeometry(410,300,300,50)
        self.txt_column.setFont(QFont('Consolas',20))
        self.txt_column.setStyleSheet('''border: 2px inset rgb(0,127,54); border-radius: 15px;''')
        self.txt_column.addItems(['ID','Model','Price','ESIM','Colour'])

        self.lb_value = QLabel('Value:',self)
        self.lb_value.setGeometry(50,360,250,50)
        self.lb_value.setFont(QFont('Consolas',20))
        self.txt_value = QLineEdit(self)
        self.txt_value.setGeometry(410,360,300,50)
        self.txt_value.setFont(QFont('Consolas',20))
        self.txt_value.setAlignment(Qt.AlignCenter)
        self.txt_value.setStyleSheet('''border: 2px inset rgb(0,127,54); border-radius: 15px;''')

        self.select_btn = QPushButton('Show info',self)
        self.select_btn.setGeometry(410,415,300,50)
        self.select_btn.setFont(QFont('Consolas',20))
        self.select_btn.setStyleSheet('''background: black; color:rgb(0,255,0); border: 2px outset rgb(0,255,0); border-radius: 15px;''')
        self.select_btn.clicked.connect(self.show_data)

        self.lb_sort = QLabel('Select sorting mode:',self)
        self.lb_sort.setGeometry(1000,300,400,50)
        self.lb_sort.setFont(QFont('Consolas',20))

        self.inc = QRadioButton('Increasing',self)
        self.inc.setGeometry(1310,360,250,50)
        self.inc.setFont(QFont('Times New Roman',20))
        self.inc.setStyleSheet('color: rgb(0,127,54);')

        self.dec = QRadioButton('Decreasing',self)
        self.dec.setGeometry(1570,360,250,50)
        self.dec.setFont(QFont('Times New Roman',20))
        self.dec.setStyleSheet('color: rgb(0,127,54);')
        
        self.sort_btn = QPushButton('Sort',self)
        self.sort_btn.setGeometry(1500,410,300,50)
        self.sort_btn.setFont(QFont("Consolas",20))
        self.sort_btn.setStyleSheet('background:black; border:2px outset rgb(0,255,0); border-radius:15px; color:rgb(0,255,0)')
        self.sort_btn.clicked.connect(self.sort_data)
        #Next window
        self.btn_window = QPushButton('Update and Delete',self)
        self.btn_window.setGeometry(1200,700,400,100)
        self.btn_window.setFont(QFont("Consolas",24))
        self.btn_window.setStyleSheet('background:black; border:2px outset rgb(0,255,0); border-radius:15px; color:rgb(0,255,0)')
        self.btn_window.clicked.connect(self.open_window)
    def base_use(self):
        self.my_con = mc.connect(host = 'localhost',user = 'root',password = 'root.702',database = 'tech')
        self.my_cur = self.my_con.cursor()
    def insert_data(self):
        self.base_use()
        sql = 'Insert into Phone(model,price,esim,colour) Values(%s,%s,%s,%s);'
        m = self.txt_model.text()
        p = int(self.txt_price.text())
        e = self.txt_esim.isChecked()
        c = self.txt_colour.currentText()
        value = (m,p,e,c)
        self.my_cur.execute(sql,value)
        self.my_con.commit()
        print('Info inserted')
        self.show_info()
    def show_data(self):
        if self.txt_column.currentText() in ('ID','Price','ESIM'):
            sql = f'Select * from Phone where {self.txt_column.currentText()} = {self.txt_value.text()}'
        else:
            sql = f'Select * from Phone where {self.txt_column.currentText()} = "{self.txt_value.text()}"'
        self.show_info(sql)
    def sort_data(self):
        if self.inc.isChecked():
            sql = f'Select * from Phone Order BY {self.txt_column.currentText()} asc'
        else:
            sql = f'Select * from Phone Order BY {self.txt_column.currentText()} desc'
        self.show_info(sql)
    def show_info(self,sql = 'Select * from Phone'):
        self.tb.setVisible(True)
        self.tb.setGeometry(50,600,850,390)
        self.tb.setColumnCount(5)
        self.tb.setHorizontalHeaderLabels(['ID','Model','Price','ESIM','Colour'])
        self.base_use()
        self.my_cur.execute(sql)
        info = self.my_cur.fetchall()
        row_c = len(info)
        ls = []
        self.tb.setRowCount(row_c)
        for x in range(row_c):
            ls.append('')
        self.tb.setVerticalHeaderLabels(ls)
        
        header = self.tb.horizontalHeader()
        for z in range(5):
            header.setSectionResizeMode(z,header.ResizeToContents)
        ver = self.tb.verticalHeader()
        ver.setDefaultAlignment(Qt.AlignCenter)
        
        for x,y in zip(range(row_c),info):
            self.tb.setItem(x,0,QTableWidgetItem(str(y[0])))
            self.tb.setItem(x,1,QTableWidgetItem(y[1]))
            self.tb.setItem(x,2,QTableWidgetItem(str(y[2])))
            if y[3]:
                s = 'ESIM'
            else:
                s = 'SIM'
            self.tb.setItem(x,3,QTableWidgetItem(s))
            self.tb.setItem(x,4,QTableWidgetItem(y[4]))
    def open_window(self):
        self.next.show()

class New_window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Update and Delete')
        self.setWindowIcon(QIcon('/home/ibrohim/Downloads/rubbish_bin.ico'))
        self.setFixedSize(1240,280)
        self.my_con = mc.connect(host = 'localhost',user = 'root',password = 'root.702',database = 'tech')
        self.my_cur = self.my_con.cursor()
        #Update
        self.lb_update = QLabel('Set:',self)
        self.lb_update.setGeometry(100,30,120,50)
        self.lb_update.setFont(QFont('',24))
        self.txt_update = QLineEdit(self)
        self.txt_update.setGeometry(270,30,300,50)
        self.txt_update.setFont(QFont('',24))
        self.txt_update.setAlignment(Qt.AlignCenter)
        self.txt_update.setStyleSheet('''border: 4px solid rgb(37,155,41); border-radius: 25px;''')

        self.lb_update2 = QLabel('Condition:',self)
        self.lb_update2.setGeometry(100,100,150,50)
        self.lb_update2.setFont(QFont('',24))
        self.txt_update2 = QLineEdit(self)
        self.txt_update2.setGeometry(270,100,300,50)
        self.txt_update2.setFont(QFont('',24))
        self.txt_update2.setAlignment(Qt.AlignCenter)
        self.txt_update2.setStyleSheet('''border: 4px solid rgb(37,155,41); border-radius: 25px;''')
        #Delete
        self.lb_delete = QLabel('Condition:',self)
        self.lb_delete.setGeometry(670,65,150,50)
        self.lb_delete.setFont(QFont('',24))
        self.txt_delete = QLineEdit(self)
        self.txt_delete.setGeometry(840,65,300,50)
        self.txt_delete.setFont(QFont('',24))
        self.txt_delete.setAlignment(Qt.AlignCenter)
        self.txt_delete.setStyleSheet('''border: 4px solid rgb(37,155,41); border-radius: 25px;''')
        #Buttons
        self.up_btn = QPushButton('Update',self)
        self.up_btn.setGeometry(200,200,300,50)
        self.up_btn.setFont(QFont("Consolas",24))
        self.up_btn.setStyleSheet('border:4px solid blue; border-radius:15px; color:blue;')
        self.up_btn.clicked.connect(self.update)

        self.del_btn = QPushButton('Delete',self)
        self.del_btn.setGeometry(740,200,300,50)
        self.del_btn.setFont(QFont("Consolas",24))
        self.del_btn.setStyleSheet('border:4px solid red; border-radius:15px; color:red;')
        self.del_btn.clicked.connect(self.delete)
    def update(self):
        txt = self.txt_update.text()
        cond = self.txt_update2.text()
        self.my_cur.execute(f'UPDATE Phone SET {txt} WHERE {cond};')
        self.my_con.commit()
        print('Changes made')
    def delete(self):
        cond = self.txt_delete.text()
        self.my_cur.execute(f'DELETE from Phone WHERE {cond};')
        self.my_con.commit()
        print('Changes made')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    t = Telephone()
    t.show()
    sys.exit(app.exec_())