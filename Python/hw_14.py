import os
from accessify import private,protected
from abc import ABC,abstractmethod
os.system("clear")

# 1-task
'''
class Employee:
    def __init__(self,n,p,s):
        self.name = n
        self.position = p
        self.salary = s
class Enterprise_employee(Employee):
    def __init__(self,n,p,s,r):
        super().__init__(n,p,s)
        self.rating = r
    def info(self):
        return f'Name: {self.name}\nPosition: {self.position}\nSalary: {self.salary}\nRating: {self.rating}'
    def bonus(self):
        if 60 <= self.rating < 75:
            self.salary += int(self.salary * 0.20)
            print("\n20% bonus added")
        elif 75 <= self.rating < 90:
            self.salary += int(self.salary * (40 / 100))
            print('\n40% bonus added')
        elif 90 <= self.rating <= 100:
            self.salary += int(self.salary * (60 / 100))
            print("\n60% bonus added")
        else:
            print('No bonus')

e = []
for x in range(int(input('Enter a number of employees: '))):
    e.append(Enterprise_employee(input('Enter full name: '),input('Enter position: '),
    int(input('Enter salary: ')),int(input('Enter rating(on a scale of 1 to 100): '))))
for y in e:
    y.bonus()
    print(y.info())
'''
# 2-task
"""
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def sleep(self):
        pass
class Tiger(Animal):
    def eat(self):
        print('Tigers primarily eat meat')
    def sleep(self):
        print('Tigers typically sleep for around 12 to 16 hours a day')
class Deer(Animal):
    def eat(self):
        print("Deer primarily eat plant material")
    def sleep(self):
        print("Deer typically sleep for around 2-3 hours per day")
class Lion(Animal):
    def eat(self):
        print('Lions primarily eat meat')
    def sleep(self):
        print("Lions typically sleep for around 16 to 20 hours a day")

t,d,l = Tiger(),Deer(),Lion()
t.eat(),t.sleep(),d.eat(),d.sleep(),l.eat(),l.sleep()
"""
# 3-task
'''
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
class Car(Vehicle):
    def start_engine(self):
        print('Insert car key into the ignition switch and turn it clockwise.')
    def stop_engine(self):
        print('Turn the key anticlockwise and remove it from the ignition switch')
class Motorcycle(Vehicle):
    def start_engine(self):
        print("Turn the ignition key to the ON position.\nPress the starter button or kick-start the bike.")
    def stop_engine(self):
        print("With the bike in neutral, turn the ignition key to the OFF position.")
c,m = Car(),Motorcycle()
print("Car")
c.start_engine(),c.stop_engine()
print('Motorbike')
m.start_engine(),m.stop_engine()
'''
# 4-task
class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass
    @abstractmethod
    def sound(self):
        pass
class Eagle(Bird):
    def fly(self):
        print('Eagles fly by using their powerful wings, which have a large wingspan and strong muscles.')
    def sound(self):
        print('Eagles make different sounds like screeching and screaming')
class Hawk(Bird):
    def fly(self):
        print('Hawks fly by using their strong wings having a large wingspan.')
    def sound(self):
        print('Hawks make various sounds such as "kee-eeeee-arr"')
e,h = Eagle(),Hawk()
print("Egles")
e.fly(),e.sound()
print('\nHawks')
h.fly(),h.sound()