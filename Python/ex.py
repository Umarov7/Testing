import os
os.system("clear")
#0002
'''
a,b = map(int,input("Enter two numbers: ").split())
if a > b:
    print(">")
elif a < b:
    print('<')
else:
    print('=')
'''    
#0010
"""
n = int(input("Enter a price: "))
a,b,c = map(int,input('Enter the amount of money: ').split())
if a+b+c >= n:
    print("Yes")
else:
    print('No')
"""
#0013
# a,b = map(int,input("Enter 2 numbers: ").split())
# day = 1
# res = 1
# while day < b:
#     res += a
#     day += 1
# print(res)
#0019
"""
n,k = map(int,input('Enter 2 numbers: ').split())
print(k//n)
"""
#0020
'''
n,k = map(int,input('Enter 2 numbers: ').split())
print(k-(k//n*n))
'''
#0022
"""
a = int(input("Enter a number: "))
print(a//10)
"""
#0023
'''
a = int(input("Enter a number: "))
print(a%10)
'''
#0053

#0119
'''
a = int(input("Enter a number: "))
if a % 4:
    print(-1)
else:
    print(a//2)
'''
#0138
"""
n = int(input("Enter a number: "))
print((n**5) + (8 * n**4) - (5 * n**3) + (3*n**2) + n - 12)
"""

# Result-Exam

# 1
def sum_numbers(s:str):
    nums = []
    temp = ''
    for i in s:
        if i.isalpha():
            if len(temp) != 0:
                nums.append(int(temp))
            temp = ''
        else:
            temp += i
    if len(temp) != 0:
        nums.append(int(temp))
    return sum(nums)
# print(sum_numbers(input('Enter a string: ')))
# 2
def textToBinary(s:str):
    ls = s.split(' ')
    temp = ''
    for i in ls:
        if i.lower() == 'nol':
            temp += '0'
        elif i.lower() == 'bir':
            temp += '1'
    print(ls,temp)
    return temp if 8 % len(temp) == 0 else ''
# print(textToBinary(input('Enter a text: ')))
# 3
def remove_letters(s:str):
    res = ''
    for l in s:
        if l not in res:
            res += l
    return res
def identical_letters(fileName):
    f = open(f'{fileName}','r')
    words = f.readline().split()
    print(words)
    res = []
    for w in words:
        if w == remove_letters(w):
            res.append(w)
    return res
# print(identical_letters('/home/ibrohim/Files/random_words'))
# 4
def cake(name:str,age:int):
    s = '*' if age % 2 else '#'
    txt = f'"{s} {age} Happy Birthday {name}! {age} {s}"'
    edge = f'"{s * (len(txt) - 2)}"'
    res = edge + '\n' + txt + '\n' + edge
    return res
# print(cake(input('Enter a name: '),int(input('Enter age: '))))
# 5
def count_animals(s:str):
    animals = ['dog','cat','bat','cock','cow','pig','fox','ant','bird',
               'lion','wolf','deer','bear','frog','hen','mole','duck','goat']
    dc = {}
    for animal in animals:
        a = set(animal)
        max_count = float('inf')
        for char in a:
            count = s.count(char) // animal.count(char)
            max_count = min(max_count, count)
        dc[animal] = max_count
    total_count = sum(dc.values())
    res = [x for x in dc.keys() if dc[x] != 0]
    return f'{total_count} {res}'
# print(count_animals(input('Enter a string: ')))
# 6
'''SELECT u1.name AS spouse1, u2.name AS spouse2, u1.address 
FROM User u1 JOIN User u2 
ON u1.address = u2.address 
WHERE u1.surname + 'a' = u2.surname and u1.age > u2.age;'''
# 7
def check_palindrome(n):
    n = str(n)
    dc = {'0':'0','6':'9','9':'6'}
    res = ''
    for x in n:
        res += dc[x]
    return n == res[::-1]
# print(check_palindrome(int(input('Enter a number: '))))
# 8
def spiral(n):
    ls = []
    for a in range(n):
        b = [0] * n
        ls.append(b)
    top,down,left,right = 0,n-1,0,n-1
    while top <= down:
        for i in range(left-1, right+1):
            ls[top][i] = 1
        for j in range(top+1, down+1):
            ls[j][right] = 1
        for k in range(right-1, left-1, -1):
            ls[down][k] = 1
        for l in range(down-1, top+1, -1):
            ls[l][left] = 1
        top += 2
        down -= 2
        left += 2
        right -= 2
    for x in ls:
        for y in x:
            print(y,end = ' ')
        print()
# spiral(int(input('Enter a number: ')))
# 9
def possible_pin(pin):
    dc = {'1':['1','2','4'],'2':['1','2','3','5'],'3':['2','3','6'],'4':['1','4','5','7'],'5':['2','4','5','6','8'],
        '6':['3','5','6','9'],'7':['4','7','8'],'8':['0','5','7','8','9'],'9':['6','8','9'],'0':['0','8']}
    if len(pin) == 1:
        return dc[pin]
    ls,res = [],[]
    for n in pin:
        ls.append(dc[n])
    print(ls)
    for x in ls[0]:
        for y in ls[1]:
            if len(ls) > 2:
                for z in ls[2]:
                    res.append(x+y+z)
            else:
                res.append(x+y)
    return res
# print(possible_pin(input('Enter PIN: ')))

# 1
from datetime import *
def Friday_13th(date):
    date = datetime.strptime(date, '%d.%m.%Y')
    while True:
        date = date.replace(day=13)
        if date.weekday() == 4:
            return date.strftime('%d.%m.%Y')
        date = date.replace(day=1) + timedelta(days=31)
# print(Friday_13th(input('Enter the date: ')))
# 2
def hex_to_binary(num):
    try:
        dc = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
        ls = [_ for _ in num]
        for x in range(len(ls)):
            if ls[x] in dc:
                ls[x] = dc[ls[x]]
            else:
                ls[x] = int(ls[x])
        dec = sum([ls[y] * (16 ** (len(ls) - y - 1)) for y in range(len(ls))])
        res = []
        while dec >= 1:
            res.insert(0, str(dec % 2))
            dec //= 2
        return ''.join(res)
    except:
        return 'ERROR'
# print(hex_to_binary(input('Enter a hexadecimal number: ')))
# 3
def typing_hands(fileName):
    f = open(fileName,'r')
    s = f.read()
    f.close()
    dc = {'Right':['6','7','Y','U','H','J','N','M','8','I','K',',','9','O','L','.','0','P',';','/'],
          'Left':['4','5','R','T','F','G','V','B','3','E','D','C','2','W','S','X','1','Q','A','Z']}
    r,l = 0,0
    for ch in s:
        if ch.isalpha():
            ch = ch.upper()
        if ch in dc['Right']:
            r += 1
        elif ch in dc['Left']:
            l += 1
    return f'Left: {l} | Right: {r}'
# print(typing_hands('/home/ibrohim/Files/words'))








# 1-task
'''ls = list(map(int,input('Enter numbers: ').split()))
print(ls)
for i in range(len(ls)-1):
    n1,n2 = str(ls[i]),str(ls[i+1])
    if n1[0] == '-' and n2[0] == '-':
        print(int(n1),int(n2))
    elif n1[0] != '-' and n2[0] != '-':
        print(int(n1),int(n2))'''

# 2-task
"""def show(n):
    print(n)
    for z in dc:
        if dc[z] == n:
            print(z,end = ' ')
    print()
names = list(map(str,input('Enter names: ').split())) # Anvar Lobar Asror Vali Surayyo Baxtiyor
values = list(map(int,input('Enter values: ').split()))
dc = {}
for x,y in zip(names,values):
    dc[x] = y
print(dc)
t,f = 0,0
for i in dc:
    if dc[i] == True:
        t += 1
    elif dc[i] == False:
        f += 1
if t > f:
    show(1)
elif f > t:
    show(0)
else:
    show(0)
    show(1)"""

# 3-task
'''f = open(input('Enter a file name: '),'r') # /home/ibrohim/Files/Emp
dt = f.readlines()
f.close()
dt = [x for x in dt if x != '\n']
for y in range(len(dt)):
    if dt[y][-1] == '\n':
        dt[y] = dt[y][:-1]
c1,c2,c3 = 0,0,0
for z in dt:
    if int(z.split()[3]) > 0 and z.split()[4][0] == '1':
        c1 += 1
    elif int(z.split()[3]) > 0 and z.split()[4][0] == '2':
        c2 += 1
    elif int(z.split()[3]) > 0 and z.split()[4][0] == '3':
        c3 += 1
m = max(c1,c2,c3)
if m == c1:
    print('1-b\'lim')
if m == c2:
    print('2-bo\'lim')
if m == c3:
    print('3-bo\'lim')'''

# 4-task
"""class Developer:
    def __init__(self,sn,p,s):
        self.surname = sn
        self.position = p
        self.salary = s
class SoftwareEngineer(Developer):
    def __init__(self,sn,p,s,b,d):
        super().__init__(sn,p,s)
        self.bonus = b
        self.department = d
    def show(self):
        return f'{self.surname} {self.position} {self.salary} {self.bonus} {self.department}'
    def income(self):
        return self.salary + self.bonus

ls = []
for i in range(5):
    sn = input('Surname: ')
    p = input('Position: ')
    s = int(input('Salary: '))
    b = int(input('Bonus: '))
    d = input('Department: ')
    ls.append(SoftwareEngineer(sn,p,s,b,d))
for j in ls:
    print(j.show())
v1 = sum(k.income() for k in ls if k.department[0] == '1')
v2 = sum(k.income() for k in ls if k.department[0] == '2')
v3 = sum(k.income() for k in ls if k.department[0] == '3')
print(f'1-bo\'lim: {v1}')
print(f'2-bo\'lim: {v2}')
print(f'3-bo\'lim: {v3}')"""

# 5-task
'''import mysql.connector as mc
class Database:
    db = None
    def __init__(self,dbName):
        self.con = mc.connect(host = 'localhost', user = 'root', password = 'root.702')
        self.cur = self.con.cursor()
        self.cur.execute(f'Create database if not exists {dbName}')
        self.con.commit()
        Database.db = dbName
    def base(self):
        self.con = mc.connect(host = 'localhost', user = 'root', password = 'root.702', database = Database.db)
        self.cur = self.con.cursor()
    def cr_table(self,tbl):
        if Database.db is not None:
            self.table = tbl
            self.base()
            sql = f"""Create table if not exists {tbl}(id int primary key auto_increment,name varchar(50),
            position varchar(50),salary int,bonus int,year real,department varchar(50),period bool)"""
            self.cur.execute(sql)
            self.con.commit()
        else:
            print('Database not found')
    def add_info(self):
        if Database.db is not None and self.table is not None:
            self.base()
            name = ['Anvar','Sardor','Davron','Kamola','Lola','Farangiz','Baxtiyor','Komil','Malika','Sharof']
            pos = ['Junior','Middle','Senior','Junior','Middle','Senior','Junior','Middle','Senior','Junior']
            sal = [500,1500,2500,500,1500,2500,500,1500,2500,500]
            bon = [100,100,-100,-100,200,-100,-100,100,100,200]
            year = [1, 0.5, 2, 0.5, 1, 2, 1, 2, 3, 0.5]
            dep = ["1-bo'lim","2-bo'lim","3-bo'lim","1-bo'lim","2-bo'lim","3-bo'lim","1-bo'lim","2-bo'lim","3-bo'lim","1-bo'lim"]
            per = [1,1,0,1,0,0,1,0,0,1]
            sql = f'Insert into {self.table}(name,position,salary,bonus,year,department,period) Values(%s,%s,%s,%s,%s,%s,%s)'
            self.cur.execute(f'Select Count(*) from {self.table}')
            row = self.cur.fetchone()[0]
            if row == 0:
                for i,j,k,l,x,y,z in zip(name,pos,sal,bon,year,dep,per):
                    self.cur.execute(sql,(i,j,k,l,x,y,z))
            else:
                print(f'Information has already been added to {self.table}')
            self.con.commit()
        else:
            print('Error occured')
    def bonus_payment(self):
        if Database.db is not None and self.table is not None:
            self.base()
            self.cur.execute(f'Select sum(bonus) from {self.table} where period = 1 or year < 1 group by department')
            res = self.cur.fetchall()
            for r in res:
                print(r[0])
        else:
            print('Error occured')
    def bonus_alike(self):
        if Database.db is not None and self.table is not None:
            self.base()
            self.cur.execute(f'Select u1 From industry Inner Join u2 From industry ON u1.bonus = u2.bonus where u1.id+1 = u2.id;')
            res = self.cur.fetchall()
            for r in res:
                print(r[0])
        else:
            print('Error occured')

ind = Database('INDUSTRY')
ind.cr_table('industry')
# ind.add_info()
ind.bonus_payment()
ind.bonus_alike()'''

# 6-task
"""def My_sort(ls):
    for i in range(len(ls)-1):
        for j in range(i+1,len(ls)):
            d1 = sum([int(x) for x in str(ls[i])])
            d2 = sum([int(y) for y in str(ls[j])])
            if d1 > d2:
                ls[i],ls[j] = ls[j],ls[i]
    return ls
try:
    nums = list(map(int,input('Enter numbers: ').split()))
except:
    print('Error occured')
print(My_sort(nums))"""

# 7-task
'''import random
n = int(input('Enter a number: '))
stones = [int(input()) for s in range(n)]
ls = []
for i in range(len(stones)):
    ls.append(stones[i] - i)
res = []
c = 0
result = None
while ls:
    if len(ls) == 0:
        result = False
    c += 1
    n = ls.pop(random.randint(0,len(ls)-1))
    res.append(n)
    if sum(res) % 3 == 0:
        if c % 2:
            result = False
        else:
            result = True
print(result)'''

def canPlaceFlowers(flowerbed, n: int) -> bool:
    if len(flowerbed) % 2 == 0:
        return False
    x = 0
    while n > 0 and x < len(flowerbed):
        if flowerbed[x] != 1:
            flowerbed[x] = 1
            n -= 1
        x += 2
    return n == 0
flower = list(map(int,input('Enter a list of 1 and 0: ').split()))
n = int(input("Enter a number: "))
print(canPlaceFlowers(flower,n))