import os
os.system('clear')
from accessify import protected, private
# 1-task
'''
class Student:
    def __init__(self,n,i,m):
        self.__name = n
        self.__id = i
        self.__marks = m
        self.__id_teacher = 123456789
    def set_name(self,n):
        self.__name = n
    def set_id(self,id):
        self.__id = id
    def get_name(self):
        print(self.__name)
    def get_id(self):
        print(self.__id)
    @protected
    def addGrade(self,gr):
        print(self.__marks)
        self.__marks.append(gr)
        print(self.__marks)
    def validation(self,id_t,g):
        if self.__id_teacher == id_t:
            self.addGrade(g)
        else:
            print("Access to marks is only provided to the teacher")

s = Student(input('Name: '),input('ID: '),list(map(int,input('Marks: ').split())))
s.validation(int(input('Teacher ID: ')),int(input("The mark you'd like to add: ")))
'''
# 2-task
'''
class Car:
    def __init__(self,c,m,y,ma):
        self.__company = c
        self.__model = m
        self.__year = y
        self.__milage = ma
    def set_company(self,c):
        self.__company = c
    def set_model(self,m):
        self.__model = m
    def set_year(self,y):
        self.__year = y
    def get_info(self):
        print(self.__company,self.__model,self.__year)
    def get_milage(self):
        print(self.__milage)
    def full_info(self):
        return f'{self.__company} - {self.__model} - {self.__year} - {self.__milage}'
    def sort_milage(ls):
        return ls.sort(key = lambda x: x.__milage,reverse = True)

cars = list()
for i in range(int(input('Enter a number of cars: '))):
    cars.append(Car(input('Brand: '),input('Model: '),int(input('Production year: ')),int(input("Milage: "))))
for x in cars:
    print(x.full_info())
Car.sort_milage(cars)
print('Result: ')
for y in cars:
    print(y.full_info())
'''
# 3-task
'''
class Circle:
    def __init__(self,r):
        self.__radius = r
    def set_radius(self,new_r):
        self.__radius = new_r
    def get_radius(self):
        print('Radius =',self.__radius)
    def calculateArea(self):
        return self.__radius ** 2 * 3.14159
    def calculatePerimeter(self):
        return self.__radius * 3.14159 * 2

c = Circle(int(input('Radius: ')))
c.get_radius()
print(f'Area = {c.calculateArea()}')
print("Perimeter = {}".format(c.calculatePerimeter()))
c.set_radius(int(input('New radius: ')))
c.get_radius()
print(f'Area = {c.calculateArea()}')
print("Perimeter = {}".format(c.calculatePerimeter()))
'''
# 4-task
class Employee:
    def __init__(self,n,i,s):
        self.__name = n
        self.__id = i
        self.__salary = s
    def set_name(self,new_n):
        self.__name = new_n
    def set_id(self,new_id):
        self.__id = new_id
    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_salary(self):
        return f'Salary: {self.__salary}'
    def sort_salary(ls):
        return ls.sort(key = lambda i: i.__salary,reverse = True)

e = []
for x in range(int(input('Enter a number of employees: '))):
    e.append(Employee(input('Name: '),input('ID: '),int(input('Salary: '))))
for y in e:
    print(f'Name: {y.get_name()} - ID: {y.get_id()} - {y.get_salary()}')
Employee.sort_salary(e)
print("Result:")
for z in e:
    print(f'Name: {z.get_name()} - ID: {z.get_id()} - {z.get_salary()}')