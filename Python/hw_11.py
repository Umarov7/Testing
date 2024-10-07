import os, random
os.system('clear')

# 1-task
'''
class animal:
    pass
class herbivore(animal):
    def info(self):
        return "Herbivore animals primarily consume plants such as leaves, stems, fruits, and seeds."
    def teeth(self):
        return 'Teeth are needed to eat plants for herbivore animals.'
    def body(self):
        return 'Herbivore animals usually have larger bodies and long necks.'    
class carnivore(animal):
    def info(self):
        return "Carnivore animals primarily consume meat."
    def teeth(self):
        return 'Teeth are needed to eat meat for carnivore animals.'
    def body(self):
        return 'Carnivore animals often have strong jaw muscles, sharp claws or teeth.'
'''
# 2-task
"""
class one:
    def __init__(self,n1 = random.randrange(1,99)):
        self.i = n1
    def show_info(self):
        print(self.i)
class two(one):
    def __init__(self,f1 = float(random.randint(1,99) - 1.247)):
        super().__init__()
        self.f = f1
    def show_info(self):
        super().show_info()
        print(self.f)
class three(two):
    def __init__(self,b1 = bool(random.randint(0,1))):
        super().__init__()
        self.b = b1
    def show_info(self):
        super().show_info()
        print(self.b)
class four(three):
    def __init__(self,s1 = 'Hello world'):
        super().__init__()
        self.s = s1
    def show_info(self):
        super().show_info()
        print(self.s)
ex = four()
ex.show_info()
"""
# 3-task
'''
class Printer:
    def __init__(self,m,s,p,k,y):
        self.model = m
        self.speed = s
        self.price = p
        self.kind = k
        self.year = y
    def info(self):
        return f'{self.model} --- {self.speed} --- {self.price} --- {self.kind} --- {self.year}'
    def sort_price(ls:list):
        ls.sort(key = lambda x: x.price)
        for y in ls:
            print(y.info())
    def year_type(ls,y,k):
        for z in ls:
            if z.year == y and z.kind == k:
                print(z.info())
p = Printer
printers = []
for _ in range(int(input('Enter a number of printers: '))):
    printers.append(Printer(input('Model: '),int(input('Speed: ')),int(input('Price: ')),input('Type: '),int(input('Year: '))))
# p.sort_price(printers)
p.year_type(printers,int(input("Enter year: ")),input("Enter type: "))
'''
# 4-task
"""
class Book:
    def __init__(self,n,a,p,p_h):
        self.name = n
        self.author = a
        self.price = p
        self.publishing_house = p_h
    def info(self):
        return f'{self.name} --- {self.author} --- {self.price} --- {self.publishing_house}'
books = []
for x in range(int(input('Enter a number of books: '))):
    books.append(Book(input('Name: '),input('Author: '),int(input('Price: ')),input('Publishing company: ')))
for y in books:
    l = y.publishing_house[0]
    if l in 'ABCDEFGH':
        print(y.info())
"""
# 5-task
'''
class Computer:
    def __init__(self,n,m,p,cpu):
        self.name = n
        self.ram = m
        self.price = p
        self.processor = cpu
    def info(self):
        return f'{self.name} --- {self.ram} --- {self.price} --- {self.processor}'
computers = list()
for x in range(int(input('Enter a number of computers: '))):
    computers.append(Computer(input('Name: '),int(input('RAM: ')),int(input('Price: ')),input('Processor: ')))
for y in computers:
    if 4 < y.ram < 16:
        print(y.info())
'''
# 6-task
class Club:
    def __init__(self,n,m,c,cap):
        self.name = n
        self.members = m
        self.coach = c
        self.captain = cap
    def info(self):
        return f'{self.name} --- {self.members} --- {self.coach} --- {self.captain}'
    def sort_name(ls:list):
        ls.sort(key = lambda x: x.name)
        for y in ls:
            print(y.info())
    def isClub(ls,n):
        c = False
        for z in ls:
            if z.name == n:
                print(z.info())
                c = True
        if c == False:
            print('There is no such club')

clubs = list()
for _ in range(int(input('Enter a number of clubs: '))):
    clubs.append(Club(input('Name: '),int(input('Number of members: ')),input('Coach: '),input('Captain: ')))
c = Club
# c.isClub(clubs,input('Enter a club name: '))
c.sort_name(clubs)