import os
os.system('clear')

# 1-task
'''
class student:
    def __init__(self,n,s,y):
        self.name = n
        self.surname = s
        self.birthyear = y
    def info(self):
        return '{} {} was born in {}'.format(self.name,self.surname,self.birthyear)
    def first_name(self):
        return self.name
    def last_name(self):
        return self.surname
    def full_name(self):
        return f'{self.name} {self.surname}'
    def age(self):
        return 2023 - self.birthyear

ls = [student('John','Smith',2001),student('Olivia','Rodrigo',2002),student('Mark','James',2003)]
for x in ls:
    print(x.info())
'''
# 2-task
"""
class Car:
    def __init__(self,m,c,w,s):
        self.model = m
        self.colour = c
        self.weight = w
        self.speed = s
    def model(self):
        return self.model
    def colour(self):
        return self.colour
    def weight(self):
        return weight
    def speed(self):
        return self.speed
    def info(self):
        return f"{self.model} - {self.colour} - {self.weight} kg - {self.speed} km/ph"
c = Car(input('Model: '),input('Colour: '),int(input('Weight: ')),int(input("Speed: ")))
print(c.info())
"""
# 3-task
'''
class Employee:
    def set_name(self):
        self.name = input('Name: ')
    def set_id(self):
        self.id = input('ID: ')
    def set_salary(self):
        self.income = int(input('Monthly income: '))
    def get_name(self):
        print(self.name)
    def get_id(self):
        print(self.id)
    def get_salary(self):
        print(self.income)
emp1,emp2,emp3 = Employee(),Employee(),Employee()
emp1.set_name()
emp1.set_id()
emp1.set_salary()
emp2.set_name()
emp2.set_id()
emp2.set_salary()
emp3.set_name()
emp3.set_id()
emp3.set_salary()
if emp1.income > emp2.income and emp1.income > emp3.income:
    emp1.get_name()
elif emp2.income > emp1.income and emp2.income > emp3.income:
    emp2.get_name()
else:
    emp3.get_name()
'''
# 4-task
"""
class Student:
    def __init__(self,n,i,m):
        self.name = n
        self.id = i
        self.mark = m
    def get_mark(self):
        return self.mark

ls = list()
for _ in range(10):
    ls.append(Student(input('Name: '),input("ID: "),int(input('Marks: '))))
ls.sort(key = lambda x: x.mark,reverse = True)    
print(ls[0].name,ls[0].id,ls[0].get_mark(), sep = '---')
"""
# 5-task
class car:
    def __init__(self,m,c,p,con):
        self.model = m
        self.colour = c
        self.price = p
        self.condition = con
    def set_speedometer(self):
        self.speedometer = input('Speedometer: ')
    def get_speedometer(self):
        print(self.speedometer)
    def full_info(self):
        return '{} - {} - {} - {} - {}'.format(self.model,self.colour,self.price,self.condition,self.speedometer)
c1 = car(input('Model: '),input('Colour: '),int(input('Price: ')),input('Condition: '))
c1.set_speedometer()
c2 = car(input('Model: '),input('Colour: '),int(input('Price: ')),input('Condition: '))
c2.set_speedometer()
print(c1.full_info(),c2.full_info(),sep = '\n')