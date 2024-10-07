import os
os.system('clear')

# 1-task
'''
class Restaurant:
    def __init__(self,n,k,l,t,m):
        self.name = n
        self.kind = k
        self.location = l
        self.w_hour = t
        self.mark = m
    def full_info(self):
        return f'{self.name} - {self.kind} - {self.location} - {self.w_hour} hours a day - {self.mark}-star'
    def info(self,name):
        print('{} is a {} restaurant situated in {}'.format(self.name,self.kind,self.location))
    def stars(self,name):
        print(f"{self.name} is a {self.mark}-star restaurant")
    def sort_time(ls:list):
        return ls.sort(key = lambda x: x.w_hour,reverse = True)
res = []
for x in range(int(input('Enter a number of restaurants: '))):
    res.append(Restaurant(input('Name: '),input('Type: '),input('Location: '),int(input('Working hours: ')),int(input('Mark: '))))
for y in res:
    print(y.full_info())
r = Restaurant
r.sort_time(res)
for z in res:
    print(z.full_info())
'''
# 2-task
"""
class Airport:
    def __init__(self,n,p,f):
        self.name = n
        self.plane = p
        self.flight = f
    def time(self,name,l:list,t_off:list):
        print(f'Time planes taking off from {self.name}:')
        for x in t_off:
            print(x)
        print(f'Time planes landing on {self.name}:')
        for y in l:
            print(y)
    def flights(self,name):
        print(f'There are {self.flight} flights at {self.name} airport per day')
    def sort_summer(self,fl:list):
        def isSummer(ls):
            if ls[1].split('.')[1] in ['06','07','08']:
                return True
            return False 
        summer = list(filter(isSummer,fl))
        summer.sort(key = lambda z: z[2])
        print(summer)
a = Airport('Tashkent International Airport',14,10)

# ls1 = ['5:30','10:00','15:30','18:59']
# ls2 = ['6:45','9:37','17:55','23:19']
# a.time(a.name,ls1,ls2)

# a.flights(a.name)

fl = list()
for x in range(int(input('Enter a number of flights: '))):
    fl.append([input('Name: '),input('Time(dd.mm): '),int(input('Price: '))])
a.sort_summer(fl)
"""
# 3-task
'''
class Time:
    def __init__(self,h,m,s):
        self.hour = h
        self.minute = m
        self.second = s
    def show(self):
        print("{:02}:{:02}:{:02}".format(self.hour,self.minute,self.second))
class Hour(Time):
    def __init__(self,h,m,s):
        super().__init__(h + 5,m,s)
class Minute(Time):
    def __init__(self,h,m,s):
        super().__init__(h,m + 5,s)
        if self.minute >= 60:
            self.minute = 0
            self.hour += 1
class Second(Time):
    def __init__(self,h,m,s):
        super().__init__(h,m,s + 5)
        if self.second >= 60:
            self.second = 0
            self.minute += 1

t = Time(int(input('Hours: ')),int(input('Minutes: ')),int(input('Seconds: ')))
t = Hour(t.hour,t.minute,t.second)
t = Minute(t.hour,t.minute,t.second)
t = Second(t.hour,t.minute,t.second)
t.show()
'''
# 4-task
"""
class Animal:
    def sound(self):
        pass
class Cat(Animal):
    def sound(self):
        print('miaow! miaow! miaow!')
class Bird(Animal):
    def sound(self):
        print("chirp! chirp! chirp!")

a = Cat()
a.sound()
a = Bird()
a.sound()
"""
# 5-task
class Employee:
    def calculate_salary(self):
        print(f'{15 * 8} $')
class Manager(Employee):
    def calculate_salary(self,time):
        print(f'{15 * time} $')
class Programmer(Employee):
    def calculate_salary(self,time):
        print(f'{15 * time} $')

e = Manager()
e.calculate_salary(int(input('Enter hours of work per day: ')))
e = Programmer()
e.calculate_salary(int(input('Enter hours of work per day: ')))