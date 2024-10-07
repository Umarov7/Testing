import random
import os
os.system("clear")

# 1-task
'''
ls = list(map(int,input("Enter the elements: ").split()))
print(ls)
sq = lambda x: x ** 2
ls = [sq(x) for x in ls]
print(ls)
'''

# 2-task
"""
ls = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
res = sorted(ls,key = lambda x: x[1])
print(ls,res,sep = '\n')
"""
# 3-task
'''
ls,odds,evens = [random.randint(10,99) for _ in range(10)],[],list()
print(ls)
o = lambda x: x % 2 
for x in ls:
    if o(x):
        odds.append(x)
    else:
        evens.append(x)    
print(odds,evens,sep = "\n")
'''
# 4-task
"""
def zeros(n:str)-> int:
    count = 0
    for x in n:
        if x == '0':
            count+=1
        else:
            break    
    return count
s = input("Enter a number as a string: ")
print('Zeros in the beginning:',zeros(s))
"""
# 5-task
'''
def convert(d_t:str)-> str:
    t = d_t.split()
    d,m,y = t[0].split(".")
    t = t[1]
    month = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',
    7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
    m,d = month.get(int(m)),int(d)
    h,mins = t.split(':')
    s = ""
    s += str(d) + ' ' + m + " " + y + ' year '
    s += str(int(h)) + ' hour ' if int(h) < 2 else str(int(h)) + ' hours '
    s += str(int(mins)) + " minutes" if int(mins) >= 2 else str(int(mins)) + " minute"
    print(s)
date_time = input("Enter the date and the time(DD.MM.YYYY HH:MM): ")
convert(date_time)
'''
# 6-task
"""
def time(sec:int)-> str:
    h = sec // 3600
    m = (sec % 3600) // 60
    s = sec % 60
    print('{:02}:{:02}:{:02}'.format(h,m,s))
t = int(input("Enter the time in seconds: "))
time(t)
"""
# 7-task
'''
def is_perfect_number(n:int)-> bool:
    ls = [x for x in range(1,n) if n % x == 0]
    return n == sum(ls)
num = int(input("Enter a number: "))
print("Perfect number:",is_perfect_number(num))
'''
# 8-task
"""
def change(num:int,n:int)-> int:
    n = str(num) + str(n)
    return int(n)
n1 = int(input("Enter a number: "))
num1 = int(input("Enter a number you'd like to add: "))
print(change(num1,n1))
"""
# 9-task
'''
def swap(x,y):
    x,y = y,x
    print(x,y)
a,b = map(int,input("Enter 2 numbers: ").split())
print(a,b)
swap(a,b)
'''
# 10-task
"""
def power(num,n):
    c = 1
    for x in range(num):
        res = n ** c
        if res == num:
            return c
        else:
            c+=1
a = int(input("Enter a number: "))
b = int(input("Enter a number you'd like to be raised: "))
print(f'{b} is raised to the power of {power(a,b)} to equal {a}')
"""
# 11-task
'''
def reverse(n:int):
    if n == 1:
        print(n)
        return
    print(n,end = ' ')
    reverse(n-1)
n = int(input("Enter a number: "))
reverse(n)
'''
# 12-task
"""
def right_order(n:int):
    if n == 1:
        print(n,end = ' ')
        return
    right_order(n-1)
    print(n,end = ' ')
n = int(input("Enter a number: "))
right_order(n)
"""
# 13-task
'''c
def reverse_even(n:int):
    if n == 0:
        print()
        return
    else:
        if n % 2 == 0:    
            print(n,end = ' ')
    reverse_even(n-1)
n = int(input("Enter a number: "))
reverse_even(n)
'''
# 14-task
def right_order_odd(n:int):
    if n != 1:
        right_order_odd(n-1)
    if n % 2:
        print(n,end = ' ')
n = int(input("Enter a number: "))
right_order_odd(n)