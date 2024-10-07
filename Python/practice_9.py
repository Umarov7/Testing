import os,random
os.system('clear')
from abc import ABC,abstractmethod

# 1-task
'''
class Shape:
    def calculate_area(self):
        pass
class Circle(Shape):
    def __init__(self,r):
        self.__radius = r
    def calculate_area(self):
        return self.__radius ** 2 * 3.14159
class Rectangle(Shape):
    def __init__(self,a,b):
        self.__a,self.__b = a,b
    def calculate_area(self):
        return self.__a * self.__b
class Triangle(Shape):
    def __init__(self,x,y,z):
        self.__x,self.__y,self.__z = x,y,z
    def calculate_area(self):
        p = (self.__x + self.__y + self.__z) / 2
        return (p * (p-self.__x) * (p-self.__y) * (p-self.__z)) * 0.5
c,r,t = Circle(15),Rectangle(13,12),Triangle(7,9,10)
print(f'C = {c.calculate_area()}\nR = {r.calculate_area()}\nT = {t.calculate_area()}')
'''
# 2-task
'''
class Animal:
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        return 'woof woof!'
class Cat(Animal):
    def sound(self):
        return 'miaow miaow!'
class Duck(Animal):
    def sound(self):
        return 'quack quack!'
d,c,du = Dog(),Cat(),Duck()
ls = [d.sound(),c.sound(),du.sound()]
print(ls)
'''
# 3-task
"""
class Vehicle:
    def rental_cost():
        pass
class Car(Vehicle):
    def __init__(self):
        self._cost = 50
    def rental_cost(self,t):
        return f'Renting a car for {t} days would cost you {self._cost * t}$'
class Bike(Vehicle):
    def __init__(self):
        self._cost = 10
    def rental_cost(self,t):
        return f'Renting a bike for {t} days would cost you {self._cost * t}$'
class Truck(Vehicle):
    def __init__(self):
        self._cost = 100
    def rental_cost(self,t):
        return f'Renting a truck for {t} days would cost you {self._cost * t}$'
c,b,t,d = Car(),Bike(),Truck(),int(input('Enter a number of days: '))
print(c.rental_cost(d),b.rental_cost(d),t.rental_cost(d),sep = "\n")
"""
# 4-task
"""
class Employee:
    def __init__(self,n,s):
        self.name = n
        self._s_hour = s
    def calculate_salary(self):
        pass
class Manager(Employee):
    def __init__(self,n,s):
        super().__init__(n,s)
    def calculate_salary(self,t):
        return f"{self.name}, as a manager, earns {(self._s_hour * t) * 20}$ a month for working for {t} hours"
class Doctor(Employee):
    def __init__(self,n,s):
        super().__init__(n,s)
    def calculate_salary(self,t):
        return f"{self.name}, as a doctor, earns {(self._s_hour * t) * 16}$ a month for working for {t} hours"
class Developer(Employee):
    def __init__(self,n,s):
        super().__init__(n,s)
    def calculate_salary(self,t):
        return f"{self.name}, as a software developer, earns {(self._s_hour * t) * 20}$ a month for working for {t} hours"
m,d,dev = Manager('Usmon',random.randint(7,15)),Doctor('Aziza',random.randrange(11,18)),Developer('Ali',random.randrange(10,19))
print(m.calculate_salary(10),d.calculate_salary(11),dev.calculate_salary(9),sep = '\n')
"""
# 5-task
'''
class Product:
    def delivery(self):
        pass
class Electronics(Product):
    def __init__(self):
        self.__cost = random.randrange(75,200)
        self._n = random.randint(1,3)
    def delivery(self):
        return f'Delivery of certain electronics would be {self.__cost * self._n}$'
class Clothing(Product):
    def __init__(self):
        self.__cost = random.randrange(20,200)
        self._n = random.randint(1,3)
    def delivery(self):
        return f'Delivery of certain clothing would be {self.__cost * self._n}$'
class Books(Product):
    def __init__(self):
        self.__cost = random.randrange(2,99)
        self._n = random.randint(1,5)
    def delivery(self):
        return f'Delivery of certain books would be {self.__cost * self._n}$'
e,c,b = Electronics(),Clothing(),Books()
print(e.delivery(),c.delivery(),b.delivery(),sep = '\n')
'''
# 6-task
'''
class BankAccount:
    def __init__(self,n,b):
        self.__name = n
        self.__balance = b
    def deposit(self,m):
        if m > 0:
            self.__balance += m
            return f'{m}$ has been deposited into the account'
        else:
            return "Error occurred"
    def withdrawal(self,m):
        if (m > 0):
            self.__balance -= m
            return f"{m}$ has been withdrawn out of the account"
        else:
            return 'Error occurred'
    def check_balance(self):
        return "Balance: {}$".format(self.__balance)
acc = BankAccount('Najim',random.randint(50,5000))
print(acc.check_balance(),acc.deposit(random.randrange(5,500)),sep = '\n')
print(acc.check_balance(),acc.withdrawal(random.randrange(5,500)),acc.check_balance(),sep = '\n')
'''
# 7-task
"""
class Employee:
    def __init__(self,n,i,s):
        self.__name = n
        self.__id = i
        self.__salary = s
    def info(self):
        print(f'Name:   {self.__name}')
        print(f'ID:     {self.__id}')
        print(f'Salary: {self.__salary}$')
    def set_salary(self,s):
        self.__salary = s
    def get_salary(self):
        return self.__salary
    def get_annual_salary(self):
        return "Annual salary: {}$".format(self.__salary * 12)
e = Employee('Ali',random.randint(1,999),random.randrange(100,1000))
e.info()
"""
# 8-task
class Vehicle(ABC):
    def __init__(self,b,m,y):
        self.brand = b
        self.model = m
        self.year = y
    @abstractmethod
    def display_info(self):
        pass
class Car(Vehicle):
    def __init__(self,b,m,y):
        super().__init__(b,m,y)
    def display_info(self):
        return f"{self.model} has been produced in {self.year} by {self.brand}"
c = Car("Ferrari",'812 Superfast',2017)
print(c.display_info())