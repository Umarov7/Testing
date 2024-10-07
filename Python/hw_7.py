import os, math
os.system('clear')
# 1
time = input('Enter the time: ')
t = time.replace(':',"")
t = str(int(t) + 1)
time = '0' + t[0] + ":" + t[1] + t[2]
while 1:
    if time == time[::-1]:
        print(time)
        break
    else:
        t = time.replace(':',"")
        t = str(int(t) + 1)
        time = '0' + t[0] + ":" + t[1] + t[2]
# 2
'''n = int(input("Enter the password: "))
if len(str(n)) != 9:
    print('no')
s = 0
for i in str(n):
    s += int(i)
s = 'yes' if s % 2 else 'no'
print(s)'''
# 3
"""t = int(input("Enter a number of tests: "))
while t:
    n = int(input("Enter a number for the test: "))
    a = 2 ** n + 3 ** n + 5 ** n + 6 ** n
    print(a ** 3)
    t-=1"""
# 4
'''n,d = map(int,input('Enter a length of the list and a date: ').split())
ls = list(map(int,input("Enter the elements: ").split()))
eq = lambda x: x == d
print(sum(filter(eq,ls)))
for y in range(n):
    if eq(ls[y]):
        print(y+1,end = ' ')'''
# 5
"""a,b = map(int,input('Enter 2 numbers: ').split())
def fact(x:int)-> int:
    s = 1
    for i in range(1,x+1):
        s *= i
    return s
def GCD(x:int,y:int):
    i,res = 1,None
    while i <= x:
        if x % i == 0 and y % i == 0:
            res = i
        i+=1    
    return res
a1 = fact(a)
b1 = fact(b)
print(GCD(a1,b1))"""
# 6
'''def CD_count(x:int,y:int):
    count = 0
    m = min(x,y)
    for i in range(1,x+1):
        if x % i == 0 and y % i == 0:
            count+=1
    return count
a,b = map(int,input("Enter 2 numbers: ").split())
print(CD_count(a,b))'''
# 7
'''def divide_by_digits(x):
    for y in str(x):
        if y == "0":
            return False
        if x % int(y):
            return False
    return True   
a,b = map(int,input("Enter 2 numbers: ").split())
ls = [x for x in range(a,b+1)]
print(len(list(filter(divide_by_digits,ls))))'''
# 8
"""n = int(input("Enter a number of elements: "))
ls = list(map(int,input('Enter the elements: ').split()))
if len(ls) == n:
    ls.remove(max(ls))
    print(max(ls))
else:
    print("The number did not match elements")"""