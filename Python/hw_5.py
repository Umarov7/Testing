import os
os.system('clear')

dc = dict()
# 1-task
'''
ls1 = list(map(str,input('Enter the first list: ').split())) # S001 S002 S003 S004
ls2 = list(map(str,input('Enter the second list: ').split(','))) # Adina Park,Leyton Marsh,Duncan Boyle,Saim Richards
ls3 = list(map(int,input('Enter the third list: ').split())) # 85 98 89 92
dc = {x : y for x,y in zip(ls2,ls3)}
ls = []
for i,j in zip(ls1,dc):
    ls.append({i : {j : dc[j]}})
print(ls)
'''
# 2-task
"""
s = input("Enter a string: ") # w3resource
dc = {s[x] : s.count(s[x]) for x in range(len(s))}
print(dc)
"""
# 3-task
'''
dc = {1:'ABC', 2:'DEF', 3:'GHI', 4:'JKL', 5:'MNO'}
v = list(dc.values())
for i in range(1,len(v),2):
    v[i],v[i-1] = v[i-1], v[i]
dc = {x : y for x,y in zip(dc.keys(),v)}
print(dc)
'''
# 4-task
"""
s = input("Enter a string: ") # Salom Yoz. Olam juda ham go'zal. Imtihon bo'lyapti.
sen = []
sen1,temp = '',[]
words = s.replace('.','').split()
for x in range(len(s)):
    if s[x] == '.':
        sen1 = ''.join(temp)
        sen.append(sen1)
        temp.clear()
    else:
        temp.append(s[x])
print(f'Words: {words}\nSentences: {sen}')
"""
# 5-task
'''
ls = list(map(int,input("Enter the numbers: ").split()))
for x in range(len(ls)-1):
    for y in range(x+1,len(ls)):
        if str(ls[x])[0] < str(ls[y])[0]:
            ls[x],ls[y] = ls[y],ls[x]
s = ''.join(str(z) for z in ls)            
print(ls,'Result: {}'.format(s),sep = '\n')
'''
# 6-task
"""
ls = [[1,'Jean Castro','V'],[2,'Lula Powell','V'],[3,'Brian Howell','VI'],[4,'Lynne Foster','VI'],[5,'Zachary Simon','VII']]
ls1 = [i[1:] for i in ls]
print(ls1)
dc = {x[0]:y for x,y in zip(ls,ls1)}
print(dc)
"""
# 7-task
'''
ls = list(map(int,input("Enter the numbers: ").split())) # 123 456 789 852 12 42 61 369
print(ls)
print('Result:',end = " ")
for x in range(len(ls)):
    if int(str(ls[x])[0]) % 2 == 0:
        print(ls[x],end = "  ")
print()
'''
# 8-task
"""
dc1 = {1:10, 2:20}
dc2 = {3:30, 4:40}
dc3 = {5:50, 6:60}
key,value = [],[]
key.extend(dc1.keys())
key.extend(dc2.keys())
key.extend(dc3.keys())
value.extend(dc1.values())
value.extend(dc2.values())
value.extend(dc3.values())
dc = {k : v for k,v in zip(key,value)}
print(dc)
"""
# 9-task
'''
n = int(input("Enter a number: "))
for i in range(1,n):
    dc.setdefault(i,i**2)
print(dc)
'''
# 10-task
"""
dc = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
mx,mn = max(dc.values()),min(dc.values())
for x,y in zip(dc.keys(),dc.values()):
    if y == mx:
        m1 = x
    elif y == mn:
        m2 = x        
dc.pop(m1)         
dc.pop(m2)
print("Result:",dc)
"""
# 11-task
'''
n = int(input("Enter a number of keys: "))
ls = list(map(int,input('Enter the values: ').split())) # 123 456 231 789 654
dc = {k : v for k,v in zip(range(1,n+1),ls)}
print(dc)
ls = sorted(list(dc.values()), reverse = True)
ls = [ls[i] for i in range(0,3)]
print("Result:",end = ' ')
for x,y in zip(dc.keys(),dc.values()):
    if y in ls:
        print(x,end = ' ')
print()
'''
# 12-task
"""
n = int(input("Enter a number of tuples: "))
ls = []
while n > 0:
    t = tuple(map(int,input('Enter the tuple: ').split()))
    ls.append(t)
    n-=1
print(ls)
for x in ls:
    ls.insert(ls.index(x),sum(x))
    ls.remove(x)
print(ls)
"""
# 13-task
'''
n = int(input("Enter a number of tuples: "))
ls = []
while n > 0:
    t = tuple(map(int,input('Enter the tuple: ').split()))
    ls.append(t)
    n-=1
print(ls)
for x in ls:
    ls.insert(ls.index(x),list(x))
    ls.pop(ls.index(x))    
print(ls)
'''
# 14-task
dc1 = {'a': 100, 'b': 200, 'c':300, 'd':100}
dc2 = {'a': 300, 'b': 200, 'd':400, 'e':200}
st = set(dc1.keys()).union(dc2.keys())
for x in st:
    if x in dc1 and x in dc2:
        dc[x] = dc1[x] + dc2[x]
    else:    
        if x in dc1:
            dc[x] = dc1[x]
        if x in dc2:
            dc[x] = dc2[x]      
print(dc)