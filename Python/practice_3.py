import os
import random
os.system('clear')
ls = list()
# 1-task
'''
ls = ['Olma', 'Uzum', 'anor', 'nok', 'behi']
ls.sort(key = str.lower)
print(ls)
'''
# 2-task
"""
ls = ['Olma', 'Uzum', 'anor', 'nok', 'behi']
for x in ls:
    if 'a' in x:
        print(x.upper(),end = " ")
print()
"""
# 3-task
'''
odds = list()
evens = []
for x in range(20):
    ls.append(random.randint(1,100))
for y in ls:
    if y % 2:
        odds.append(y)
    else:
        evens.append(y)
print(ls)
print(odds)
print(evens)
'''
# 4-task
"""
n = []
for x in range(20):
    ls.append(random.randint(1,100))
for y in ls:
    if y % 3 == 0 and y % 5 == 0:
        n.append(y)
print(ls)
print(n)
print(n[::-1])
"""
# 5-task
'''
for i in range(1,11):
    ls.append(i)
print(ls)
ls.clear()
for j in range(10):
    ls.append('hi')
print(ls)
'''
# 6-task
"""
l1 = [random.randint(1,9) for x in range(10)]
l2 = [random.randint(1,9) for x in range(10)]
print(l1)
print(l2)
for y in l1:
    if y % 2 == 0:
        l2.append(y**2)
print(l2)
"""
# 7-task
'''
l1 = list()
l2 = []
words = ["katta-kichik", "aka-uka", "ota-ona", "opa-singil"]
for x in words:
    temp = x.split('-')
    l2.append(temp[0])
    l1.append(temp[1])
print(l1)
print(l2)
'''
# 8-task
"""
l1 = ['Olma', 'Uzum', 'anor', 'nok', 'behi']
l2 = ['nok', 'behi']
l1,l2 = l2,l1
print(l1)
print(l2)
"""
# 9-task
'''
ls = ['Olma', 'Uzum', 'anor', 'nok', 'behi']
for x in ls:
    y = x.lower()[::-1] if x.count('m') != 0 else 0
    if y != 0:
        print(y,end = ' ')
print()
'''
# 10-task
ls = [2, 4, 6, 8, 10]
n = int(input("Enter a number between 1 and 10: "))
n = ls.index(n) if n % 2 == 0 else ls.index(n+1)
print(n)