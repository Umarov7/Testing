import random
import os
os.system("clear")

ls = []
# 1-task
'''
a,b = map(int,input("Enter 2 numbers: ").split())
for i in range(a,b):
    if i % 2 == 0:
        ls.append(i)
print(ls)
'''
# 2-task
"""
a,b = map(int,input("Enter 2 numbers: ").split())
while b > a:
    if b % 2:
        ls.append(b)
    b-=1
print(ls)
"""
# 3-task
'''
n = int(input('Enter a number of elements: '))
while n > 0:
    num = int(input(">>> "))
    if ls.count(num) == 0:
        ls.append(num)
    n-=1
ls.sort()
print(ls)
'''
# 4-task
"""
n = int(input('Enter a number of elements: '))
ls = [random.randint(1,99) for _ in range(n)]
print(ls)
for x in ls:
    prm_1 = True
    j = 2
    while j*j <= x:
        if x % j == 0:
            prm_1 = False
            break
        j+=1
    if prm_1 == True:
        prm_1 = x
        break
for y in ls:
    prm_2 = True
    j = 2
    while j*j <= y:
        if y % j == 0:
            prm_2 = False
            break
        j+=1
    if prm_2 == True:
        prm_2 = y
print("The first and last prime numbers: ",prm_1,prm_2,end = ' ')
"""
# 5-task
'''
n = int(input('Enter a number: '))
f1,f2 = 0,1
ls = [f1,f2]
for x in range(2,n):
    ls.append(ls[-1] + ls[-2])
print(ls)
print('Sum of elements =',sum(ls))
'''
# 6-task
"""
ls = input('Enter a string: ').split()
for x in ls:
    if len(x) % 2:
        print(x[::-1])
"""
# 7-task
'''
ls = input('Enter a string: ').split()
ls.sort()
print(ls)
'''
# 8-task
ls = input('Enter a string: ').split()
ls.sort(key = len)
ls.reverse()
print(ls)