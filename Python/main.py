import os
import random, math
os.system("clear")
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
#res = bool (a//b) * a + bool (b//a) * b
#print(f"Max({a},{b}) =",res)

#time = int(input("Enter the time in seconds: "))
#h = time // 3600
#m = (time % 3600) // 60
#s = time % 60
#print("{:02d}:{:02d}:{:02d}".format(h,m,s))
"""
a = int(input("Enter a number: "))
p = a*4
s = a*a
print("P =",p)
print("S =",s)
"""
'''
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
p = (a+b) * 2
s = a*b
print("P =",p)
print("S =",s)
'''
"""
d = int(input("Enter a number: "))
l = d * 3.14
print("L =",l)
"""
'''
a = int(input("Enter a number: "))
v = a ** 3
s = a ** 2 * 6
print("V =",v)
print("S =",s)
'''
"""
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
v = a*b*c
s = (a*b + b*c + c*a) * 2
print("V =",v)
print("S =",s)
"""
# r = int(input("Enter a number: "))
# l = r * 3.14 * 2
# s = r ** r * 3.14
# print("L =",l)
# print("S =",s)



# n = int(input("Enter a number: "))
# sum_e = 0
# pro_o = 1
# i = 1
# while i <= n:
#     if i % 2:
#         pro_o *= i
#     else:
#         sum_e += i
#     i += 1
# print("Sum of evens: ",sum_e)
# print("Product of odds: ",pro_o)
'''
n = int(input("Enter a number: "))
print((n**5) + (8 * n**4) - (5 * n**3) + (3*n**2) + n - 12)
'''
"""
n = int(input("Enter a number: "))
sum = 0
for i in range(1,n):
    if(n % i == 0 and i % 2):
        sum += i
print(f"Sum of odd numbers divisible by {n} = ",sum)
"""

# text = input("Enter a string: ")
# sum = 0
# for j in range(len(text)):
#     if ord(text[j]) > 47 and ord(text[j]) < 58:
#         sum += int(text[j])
# print("Sum of digits = ",sum)
'''
ls = list()
n = int(input("Enter a number of elements: "))
while n > 0:
    ls.append(random.randint(10,99))
    n-=1
print(ls)
avg = sum(ls) / len(ls)
print("Average:",avg)
for i in ls:
    if i < avg:
        print(i,end = ' | ')
print()
'''
"""
ls = []
n = int(input("Enter a number of elements: "))
while n > 0:
    ls.append(random.randint(10,99))
    n-=1
print(ls)
print("Result: ",end = "")
for i in range(1,len(ls),2):
    if ls[i] % 2 == 0:
        print(ls[i],end = " | ")
print()
"""


'''
s = list(map(int,input("Enter the orders: ").split()))
f = list(map(int,input("Enter the meals: ").split()))
print("Orders:",s)
print("Meals:",f)
while f[0] in s:
    s.remove(f[0])
    f.pop(0)
    if len(f) == 0:
        break
print("Left Orders:",s)
print("Left Meals:",f)
'''
"""
ls = list(map(int,input("Enter the elements: ").split()))
res = ls.copy()
for x in res:
    if (ls.count(x) > 1):
        continue
    else:    
        ls.remove(x)
print(ls)
"""
'''
l1 = list(map(int,input("Enter the first list: ").split()))
l2 = list(map(int,input("Enter the second list: ").split()))
s,b = 0,0
for x in range(len(l1)):
    if l1[x] == l2[x]:
        s += 1
    elif l2[x] in l1:
        b += 1
print(f"{s}S{b}B")
'''
"""
ls = list(map(int,input("Enter the elements: ").split()))
print(ls)
res = []
for x in ls:
    res.append(ls[x])
print(res)
"""
'''
n1,n2 = map(int,input("Enter 2 numbers: ").split())
num1,num2 = n1,n2
c1,c2 = 0,0
l1,l2 = [],[]
while True:
    while n1 != 1:
        if n1 % 2 == 0:
            n1 = n1 // 2
            l1.append(n1)
        else:
            n1 = n1 * 3 + 1
            l1.append(n1)
        c1+=1      
    while n2 != 1:        
        if n2 % 2 == 0:
            n2 = n2 // 2
            l2.append(n2)
        else:
            n2 = n2 * 3 + 1
            l2.append(n2)
        c2+=1
    break        
if c1 < c2:
    print(num1,c1)
elif c2 < c1:
    print(num2,c2)
else:
    print('Equal')    
print(l1,l2)
'''
"""
ls = [('Str',"45",False),('456',36.25,"54",True),(36,25,14.254,None),(11,0,"False")]
for x in range(4):
    for y in range(len(ls[x])):
        # print(f"{ls[x][y]}",end = ' | ')
        if type(ls[x][y]) == int or type(ls[x][y]) == float:
            print(ls[x][y])
"""



# st = set()
'''
st = {random.randint(10,99) for x in range(20)}
print(st)
over = True
while over:
    over = False
    for x in st:
        isprime = True
        j = 2
        while j * j <= x:
            if x % j == 0:
                isprime = False
                break
            j+=1
        if isprime == True:
            st.remove(x)
            over = True
            break
print(st)
'''
dc = {} # dict()
'''
n = int(input('Enter a number: '))
for x in range(n):
    k,v = map(str,input("Enter the key and the value: ").split())
    v = int(v)
    dc.setdefault(k,v)
print(dc)
'''
"""
s = input("Enter a string: ")
ls = list(map(str,input("Enter the words: ").split()))
s = s.split()
for x in ls:
    count = s.count(x)
    dc.setdefault(x,count)    
print(dc)
"""



# def Max(n1,n2)->int:
#     return max(n1,n2)
# n1,n2 = map(int,input("Enter 2 numbers: ").split()) 
# print(f'Max{n1,n2} = {Max(n1,n2)}')
'''
def debit_card(n:int):
    res = str()
    while 1:
        if len(res) == 4:
            break
        res += str(n % 10)
        n //= 10
    res = res[::-1]    
    for x in range(12):
        res = '*' + res
    return res
n = int(input('Enter the card: ')) # 8600312958176554
print(debit_card(n))
'''
"""
ls = [random.randint(1,99) for x in range(20)]
print(ls)
def isprime(n:int)-> bool:
    if n <= 1:
        return False
    j = 2
    while j * j <= n:
        if n % j == 0:
            return False
        j+=1
    return True
res = list(filter(isprime,ls))
print(res)
"""
'''
ls = [random.randint(1,99) for x in range(7)]
def seven(ls1:list)-> bool:
    if 7 in ls1:
        return True
    for x in ls1:
        if '7' in str(x):
            return True
    return False
print(seven(ls))
'''



from colorama import Fore,Back,Style, init
# init.
# print(Fore.BLUE + Back.BLACK + "Uzbekistan")
# print(Fore.WHITE + Back.BLACK + "tengdir")
# print(Fore.GREEN + Back.BLACK + "Uzbekistanga")
# import sys, math, random
# sys.stdout.write(Fore.GREEN + 'Hi\n') # UTF-8 192.168.0.1
# print(sys.version)
# print(sys.path)
# print(dir(random))
# print(sys.exit())
'''
while 1:
    try:
        age = int(input("Enter your age: "))
        if age > 0:
            break
    except:
        print("Try again!")
print(age)
'''



'''
os.chdir("/home/ibrohim/Files_py")
try:
    f = open("Numbers.txt",'x')
    for x in range(100):
        f.write(str(random.randint(1,100)) + ' ')
    f.close()
    print("The info has successfully been written")
except:
    print('The file already exists')
'''
"""
os.chdir("/home/ibrohim/Files_py")
try:
    def mac_address(s):
        count = 0
        with open('Internet_mac.txt','wt') as m_a:
            for x in s:
                m_a.write(f"{x.split(',')[2]}\n")
                count += 1
        return count    
    f = open('/home/ibrohim/Downloads/Telegram Desktop/Internet.txt','r')
    print('Mac addresses: {}'.format(mac_address(f.readlines())))
except:
    print("Error occured")
"""
'''
with open("/home/ibrohim/Downloads/Telegram Desktop/Internet.txt","rt") as f:
    ls,dc = [],{}
    l = f.readlines()
    for x in l:
        y = x.split(",")[3]
        ls.append(y.split("\n")[0])
    for z in ls:
        dc[z] = ls.count(z)
print(dc)      
item = list(dc.items())
dc = sorted(item,key = lambda x: x[1],reverse = True)
print(dc)
'''


'''
def sea_battle(ls:list,target):        
    dc = {"A":0,"B":1,"C":2,"D":3,"E":4}
    return 'BOOM' if ls[dc[target[0]]][int(target[1])-1] == '*' else "SPLASH"
ls = [  [".", ".", ".", "*", "*"],
        [".", "*", ".", ".", "."],
        [".", "*", ".", ".", "."],
        [".", "*", ".", ".", "."],
        [".", ".", "*", "*", "."]]        
print(ls)        
t = input("Enter the coordination(Ex:A1): ")
print(sea_battle(ls,t))
'''
# def pin_code(p:str):
#     dc = {'0':["0","8"],'1':["1","2","4"],'2':["1","2","3","5"],'3':["2","3","6"],'4':["1","4","5","7"],
#     '5':["2","4","5","6","8"],'6':["3","5","6","9"],'7':["4","7","8"],'8':["0","5","7","8","9"],'9':["6","8","9"]}
#     res = []
#     for x in dc[p[0]]:
        
#     return res
# pin = input('Enter the pin: ')
# pin_code(pin)

'''
def painting(ls:list):
    t,y = 0,None
    for x in ls:
        t += 2
        if x != y and y is not None:
            t += 1
        y = x
    return t
colours = list(map(str,input("Enter colours: ").split()))
print(painting(colours))
'''

"""
f = open("/home/ibrohim/Downloads/Telegram Desktop/FILE_MOC.txt",'rt')
for x in f.readlines():
    y = x.split(',')
    nat = y[4].split('\n')[0]
    if nat == 'German' and y[2] == "Female" and int(y[3].split(".")[2]) < 1973:
        print(x)
"""




'''
class book:
    def __init__(self,au,ge,pa):
        self.author = au
        self.genre = ge
        self.pages = pa
    def info(self):
        return '{}-page {} book by {}'.format(self.pages,self.genre,self.author)
    def finish(self,daily):
        print(f"The book will be finished in {math.ceil(self.pages / daily)} days if {daily} pages are read daily")

the_book = book('J.K.Rowling','Fantasy',250)
print(the_book.info())
the_book.finish(15)
'''
"""
class laptop:
    def __init__(self,br,me,pr):
        self.brand = br
        self.memory = me
        self.price = pr
class smartphone(laptop):
    def __init__(self,b,m,p,e_s):
        super().__init__(b,m,p)
        self.e_sim = e_s

phone = smartphone
ls = []
i = 1
while i == 1:
    phone.brand = input('Brand: ')
    phone.memory = int(input('Memory: '))
    phone.price = int(input('Price: '))
    phone.e_sim = int(input('E_SIM: '))
    ls.append(phone)
    i = int(input("Enter 1 if you wanna continue >>> "))
def show(cl:smartphone):
    print(cl.brand,cl.memory,cl.price,cl.e_sim)
    print(80*'*')
for x in ls:
    print(show(x))
"""




'''
class Student:
    def __init__(self,n):
        self.name = n
    def working_hour(self):
        print(f'{self.name} works/studies 5 hours a day')
class Teacher:
    def __init__(self,n):
        self.name = n
    def working_hour(self):
        print(f'{self.name} works 8 hours a day')
class Doctor:
    def __init__(self,n):
        self.name = n
    def working_hour(self):
        print(f'{self.name} works 10 hours a day')
s = Student(input('Enter name: '))
t = Teacher(input('Enter name: '))
d = Doctor(input('Enter name: '))
s.working_hour()
t.working_hour()
d.working_hour()
'''
"""
class Shape:
    def __init__(self):
        print('Object has been initialised from Shape class')
    def sq(self):
        print('Square of each shape should be calculated separately')
class Square(Shape):
    def __init__(self,a):
        self.q = a
        print(f'Each side of square is {self.q} sm')
    def sq(self):
        return self.a * self.a
class Triangle(Shape):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.check = a+b > c and a+c > b and b+c > a   
    def sq(self):
        if self.check == False:
            return None
        else:
            p = (self.a + self.b + self.c) / 2
            s = p * (p - self.a) * (p - self.b) * (p - self.c)
            return s ** 0.5
"""
'''
class Car:
    def __init__(self,s,f):
        self.speed = s
        self.fuel = f
    def time(self,distance):
        print('A car will reach the destination in {:.1f} hours'.format(distance / self.speed))
        print(f"A car will use {distance * self.fuel} litres of fuel")
class Motorbike(Car):
    def __init__(self,s,f):
        super().__init__(s,f)
    def time(self,distance):
        print('A motorbike will reach the destination in {:.1f} hours'.format(distance / self.speed))
        print(f"A motorbike will use {distance * self.fuel} litres of fuel")
class Bike(Motorbike):
    def __init__(self,s):
        self.speed = s
    def time(self,distance):
        print('A bike will reach the destination in {:.1f} hours'.format(distance / self.speed))

d = int(input("Enter the distance in kilometres: "))
c = Car(int(input('Enter the speed per kilometre: ')),int(input('Enter the fuel per kilometre: ')))
m = Motorbike(int(input('Enter the speed per kilometre: ')),int(input('Enter the fuel per kilometre: ')))
b = Bike(int(input('Enter the speed per kilometre: ')))
c.time(d)
m.time(d)
b.time(d)
'''
"""
class Shape:
    def draw(self):
        print('No such shape found')
class Line(Shape):
    def draw(self):
        print(60 * '*')
class Triangle(Shape):
    def draw(self):
        for x in range(1,10):
            for y in range(1,10):
                if y == 1 or x == y or x == 9:
                    print('*',end = ' ')
                else:
                    print(' ',end = ' ')
            print()    
class Rectangle(Shape):
    def draw(self):
        for x in range(1,10):
            for y in range(1,15):
                if x == 1 or y == 1 or x == 9 or y == 14:
                    print('*',end = ' ')
                else:
                    print(' ',end = ' ')
            print()
class Square(Shape):
    def draw(self):
        for x in range(1,9):
            for y in range(1,10):
                if x == 1 or y == 1 or x == 8 or y == 9:
                    print('*',end = ' ')
                else:
                    print(' ',end = ' ')
            print()

sh = input("Enter a shape name: ")
if sh == 'line':
    l = Line()
    l.draw()
elif sh == 'triangle':
    t = Triangle()
    t.draw()
elif sh == 'rectangle':
    r = Rectangle()
    r.draw()
elif sh == 'square':
    s = Square()
    s.draw()
else:
    s = Shape()
    s.draw()
"""



'''
class Television:
    def turn_on(self):
        print('TV has been turned on')
        self.__music()
        self.__ads()
        self.__film()
        self.__ads()
    def __music(self):
        print('Music is playing')
    def __ads(self):
        print('Product is being advertised')
    def __film(self):
        print('Film is being aired')

TV = Television()
TV.turn_on()
'''
"""
class Plant:
    def __init__(self,n):
        self.name = n
        self.calorie = random.randint(2,15)
    def feed(self):
        return self.calorie
class Animal:
    def __init__(self,n):
        self.name = n
        self.__energy = random.randint(1,99)
        print(f"Energy: {self.__energy}")
    def food(self,en):
        if self.__energy < 70:
            self.__energy += en
            print("{}'s energy has reached {}".format(self.name,self.__energy))
        else:
            print(f'{self.name} is already full')

pl = Plant(input('Type of plant: '))
an = Animal(input('Animal name: '))
an.food(pl.calorie)
"""
'''
class Person:
    def setter(self,x,y,z):
        self._name = x
        self._age = y
        self._country = z
    def getter(self):
        print(f'Name - {self._name}\nAge - {self._age}\nCountry - {self._country}')

p = Person()
p.setter(input('Name: '),int(input('Age: ')),input('Country: '))
p.getter()
'''
"""
class Rectangle:
    def setter(self,a,b):
        self.__length = a
        self.__width = b
    def getter(self):
        print('Length = {}\nWidth = {}'.format(self.__length,self.__width))
    def perimeter(self):
        return (self.__length + self.__width) * 2
    def square(self):
        return self.__length * self.__width

r = Rectangle()
r.setter(int(input("Enter the length of a rectangle: ")),int(input("Enter the width of a rectangle: ")))
r.getter()
print(f'P = {r.perimeter()}\nS = {r.square()}')
"""
from accessify import private
from accessify import protected
'''
class Patient:
    __doctor = {1234:'Akramov Salim'}
    def __init__(self):
        self.name = 'Abdullayev Karim'
        self.__diagnose = 'Heart failure'
        self.__balance = 15200000
        self.__ID_doctor = 1234
    @protected
    def info(self,id):
        print(f'Name:       {self.name}')
        print(f'Diagnose:   {self.__diagnose}')
        print(f'Balance:    {self.__balance}')
        print(f'ID(doctor): {self.__ID_doctor}')
    def check(self,id):
        if id == self.__ID_doctor:
            self.info(id)
        else:
            print('Information about patients are only provided to doctors')
class Doctor:
    def __init__(self,id):
        self._id = id
        Patient().check(self.get_id())
    def get_id(self):
        return self._id
d = Doctor(1234)
'''
"""
class Credit:
    def __init__(self,name,c):
        self.creditor = name
        self.credit = c
class Client(Credit):
    def __init__(self,n,b):
        self.name = ''
        self.balance = b
    def lend_money(self,cr):
        self.balance += cr
        print(f'Balance has been updated: {self.balance}')

cr = Credit(input('Creditor: '),int(input('Credit: ')))
cl = Client(input('Client: '),int(input('Balance: ')))
cl.lend_money(cr.credit)
"""





from abc import ABC, abstractmethod
'''
class Phone(ABC):
    @abstractmethod
    def info(self):
        pass
    @abstractmethod
    def price(self):
        pass
class Samsung(Phone):
    def info(self):
        return "Samsung Galaxy A7 2017"
    def price(self):
        return 'Price: 100$'
class iPhone(Phone):
    def info(self):
        return "iPhone 6 2014"
    def price(self):
        return 'Price: 100$'

s = Samsung()
i = iPhone()
print(s.info())
print(s.price())
print(i.info())
print(i.price())
'''
"""
class BankAccount(ABC):
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdrawal(self):
        pass

class SavingsAccount(BankAccount):
    def __init__(self,b):
        self.balance = b
        self.__pin = 1234
    def deposit(self,s):
        self.balance += s
        return 'Deposit account balance: {}'.format(self.balance)
    @protected
    def withdrawal(self,s):
        self.balance -= s
        return "Deposit account balance: {}".format(self.balance)
    def check_pin(self,s1,p):
        if self.__pin == p:
            return self.withdrawal(s1)
        else:
            return 'Wrong PIN number'
class CurrentAccount(BankAccount):
    def __init__(self,b):
        self.balance = b
        self.__pin = 4321
    def deposit(self,s):
        self.balance += s
        return f"Current account balance: {self.balance}"
    @protected
    def withdrawal(self,s):
        self.balance -= s
        return f'Current account balance: {self.balance}'
    def check_pin(self,s2,p):
        if self.__pin == p:
            return self.withdrawal(s2)
        else:
            return 'Wrong PIN number'

s = SavingsAccount(int(input('Enter a balance of deposit(savings) account: ')))
print(s.deposit(int(input('Enter a sum of deposit into deposit(savings) account: '))))
print(s.check_pin(int(input('Enter a sum of withdrawal from deposit(savings) account: ')),int(input('Enter PIN: '))))
print('\n')
c = CurrentAccount(int(input('Enter a balance of current account: ')))
print(c.deposit(int(input('Enter a sum of deposit into current account: '))))
print(c.check_pin(int(input('Enter a sum of withdrawal from current account: ')),int(input('Enter PIN: '))))
"""
'''
class Student:
    def __init__(self):
        self._name = ''
        self.__age = 0
    @property
    def info(self):
        return f'Name: {self._name}\nAge: {self.__age}'
    @info.setter
    def info(self,x):
        self._name = x[0]
        self.__age = x[1]
    @info.deleter
    def info(self):
        del self._name, self.__age
        print('Info has been deleted')

s = Student()
print(s.info)
s.info = (input('Enter name: '),int(input('Enter age: ')))
print(s.info)
del s.info
print(s.info)
'''
"""
class Music(ABC):
    @abstractmethod
    def info(self):
        pass
class Pop(Music):
    def __init__(self,s,l):
        self.__singer = s
        self._length = l
    def info(self):
        print(f'A {self._length} pop song by {self.__singer}')
class Hip_Hop(Music):
    def __init__(self,s,l):
        self.__singer = s
        self._length = l
    def info(self):
        print("A {} hip-hop song by {}".format(self._length,self.__singer))

p = Pop(input('Singer: '),input('Length: '))
p.info()
h = Hip_Hop(input('Singer: '),input('Length: '))
h.info()
"""



'''
class Market:
    def __init__(self,k,a,s):
        self.kind = k
        self.address = a
        self.staff = s
    def info(self):
        print(f'Type: {self.kind}\nAddress: {self.address}\nNumber of staff members: {self.staff}')
class Shop(Market):
    def __init__(self,k,a,s,t):
        super().__init__(k,a,s)
        self.time = t
    def info(self):
        super().info()
        print("Working hours: {}".format(self.time))
class Restaurant(Market):
    def __init__(self,k,a,s,t):
        super().__init__(k,a,s)
        self.time = t
    def info(self):
        super().info()
        print("Working hours: {}".format(self.time))
m = Market(input('Enter type: '),input('Enter address: '),int(input('Enter staff number: ')))
s = Shop(input('Enter type: '),input('Enter address: '),int(input('Enter staff number: ')),int(input('Enter open hours: ')))
r = Restaurant(input('Enter type: '),input('Enter address: '),int(input('Enter staff number: ')),int(input('Enter open hours: ')))
m.info()
s.info
r.info()
'''
"""
class Shop:
    def __init__(self,n,s,i,p):
        self.name = n
        self.staff = s
        self.daily_income = i
        self.percent = p
        self.pay = 3
    def info(self):
        print(f'Name: {self.name}\nNumber of staff members: {self.staff}')
        print("Daily revenue: {}".format(self.revenue()))
    def revenue(self):
        total_wage = self.staff * self.pay
        return self.daily_income * (self.percent / 100) - total_wage
class Restaurant:
    def __init__(self,n,s,i,p):
        self.name = n
        self.staff = s
        self.daily_income = i
        self.percent = p
        self.pay = 3
    def info(self):
        print(f'Name: {self.name}\nNumber of staff members: {self.staff}')
        print("Daily revenue: {}".format(self.revenue()))
    def revenue(self):
        total_wage = self.staff * self.pay
        return self.daily_income * (self.percent / 100) - total_wage
s = Shop(input('Enter name: '),int(input('Enter staff number: ')),int(input('Enter daily income: ')),int(input('Enter revenue percent: ')))
os.system('clear')
r = Restaurant(input('Enter name: '),int(input('Enter staff number: ')),int(input('Enter daily income: ')),int(input('Enter revenue percent: ')))
os.system('clear')
s.info(),r.info()
"""