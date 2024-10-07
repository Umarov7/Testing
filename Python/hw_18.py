import os, sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

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