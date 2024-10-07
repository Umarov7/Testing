import random
import os
os.system('clear')

t = tuple()
# 1-task
'''
t = list()
t = [random.randint(1,50) for x in range(10)]
t = tuple(t)
print(t)
for x in t:
    print(t[3],t[len(t)-4],end = " ")
    break
print()
'''
# 2-task
"""
ls,t = list(),list()
i = 0
while i < 3:
    t = [random.randint(1,50) for x in range(3)]
    ls.append(tuple(t))
    i+=1
print(ls)
ls = [tuple(list(x)[:-1] + [100]) for x in ls]
print(ls)
"""
# 3-task
'''
ls = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
print(ls)
i = len(ls)-1
while i >= 0:
    if len(ls[i]) == 0:
        ls.pop(i)
    i-=1
print(ls)
'''
# 4-task
"""
ls = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5'), ('item0', '23.15')]
# from operator import itemgetter
# ls = sorted(ls,key = itemgetter(1), reverse = True)
for x in range(len(ls)-1):
    for y in range(x+1,len(ls)):
        if float(ls[x][1]) < float(ls[y][1]):
            ls[x],ls[y] = ls[y],ls[x]
print(ls)
"""
# 5-task
'''
s = input('Enter a string: ').replace(" ","")
t = tuple(x for x in s)
print(t)
'''
# 6-task
"""
ls = [(1,2), ('s','a','l'), ('13','123',True,"String"), ('a', 'b'), ('a', 'b', 'c'), ('d')]
print(ls)
ls.sort(key = len,reverse = True)
print('Result:',ls)
"""