import os,random
os.system('clear')

class Admin:
    __count = 0
    def __init__(self):
        Admin.__count += 1
        self.__name = None
        self.__id = Admin.__count
        self.__marks = None
        self.__pay_st = None
    @property
    def student(self):
        return f'Name: {self.__name}\nID: {self.__id}\nMarks: {self.__marks}\nPayment status: {self.__pay_st}'
    @student.setter
    def student(self,info):
        self.__name = info[0]
        self.__marks = info[1]
    @student.deleter
    def student(self):
        del self.__name, self.__id, self.__marks, self.__pay_st
        print('Info has been deleted')
    def change_marks(self,i,s,m):
        if self.__id == i:
            print('Would you like to add or change already existing subjects and marks? (1: Add 2: Change)')
            op = int(input('>>> '))
            if (op == 1):
                for i,j in zip(s,m):
                    self.__marks[i] = j
                print('Changes applied to subjects and marks')
            elif op == 2:
                self.__marks = {}
                for i,j in zip(s,m):
                    self.__marks[i] = j
                print('Changes applied to subjects and marks')
            else:
                print('Invalid operation')
        else:
            print('Invalid ID')
    def payment_status(self,i):
        if self.__id == i:
            s = int(input('(Unpaid: 0 Paid: 1) >>> '))
            if s == 0:
                self.__pay_st = False
                print("Payment status changed")
            elif s == 1:
                self.__pay_st = True
                print("Payment status changed")
            else:
                print('Invalid operation')
        else:
            print('Invalid ID')
    def find_failed(self):
        for x in self.__marks:
            if self.__marks[x] < 60:
                return "Failed"
        return 'Passed'
    def find_top(self):
        for y in self.__marks:
            if self.__marks[y] <= 86:
                return 'Not a top student'
        return "Top student"
    def display_info(self,i):
        if self.__id == i:
            return self.student
        else:
            return 'Invalid ID'

a = Admin()
a.student = ("Ali",{'History':88,'Math':75,'English':93,'Physics':70})
# x = ['Programming','Biology','Chemistry','Geography']
# y = [random.randint(50,100) for a in range(len(x))]
# a.change_marks(7,x,y)

# a.payment_status(7)
# print(a.find_failed())
# print(a.find_top())
# print(a.display_info(1))