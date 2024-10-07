import os
os.system("clear")

# 1-task
f = open('/home/ibrohim/Downloads/FULL_NAME.txt','r')
dt = f.readlines()
res = sorted(dt,key = lambda x: x.split()[1])
for n in res:
    print(n)
f.close()
# 2-task
"""
f = open('/home/ibrohim/Downloads/Karta.txt','r')
dc = {}
dt = f.readlines()
for x in dt:
    y = x.split(',')[5]
    y = y.split('\n')[0]
    dc[y] = dc.get(y, 0) + 1
print(dc)
f.close()
"""
# 3-task
'''
f = open('/home/ibrohim/Downloads/Karta.txt','r')
ls = []
dt = f.readlines()
for x in dt:
    y = x.split(',')[5]
    y = y.split('\n')[0]
    if x.split(',')[1] == 'visa':
        ls.append(y)
ls.sort()
for z in ls:
    while ls.count(z) > 1:
        ls.remove(z)
for a in ls:
    print(a)
f.close()
'''
# 4-task
"""
f = open('/home/ibrohim/Downloads/Karta.txt','r')
ls = ['0','1','2','3','4','5','6','7','8','9']
dt = f.readlines()
for x in dt:
    y = x.split(',')[0]
    cou = x.split(',')[5]
    cou = cou.split('\n')[0]
    if all(z in y for z in ls):
        print(y, cou, x.split(',')[2], x.split(',')[4],sep = '___')
f.close()
"""
# 5-task
'''
f = open('/home/ibrohim/Downloads/car.txt','r')
dt = f.readlines()
dc = {}
for x in dt:
    y = x.split(',')[4]
    y = y.split('\n')[0]
    dc[y] = dc.get(y,0) + 1 
print(dc)
f.close()
'''
# 6-task
"""
f = open('/home/ibrohim/Downloads/car.txt','r')
dt = f.readlines()
res = sorted(dt,key = lambda z: z.split(',')[2],reverse = True)
for i in res:
    m = i.split(',')[1]
    y = i.split(',')[2]
    c = i.split(',')[4]
    c = c.split('\n')[0]
    print(m,c,y,sep = '____')
f.close()
"""