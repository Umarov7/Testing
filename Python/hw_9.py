import os
os.system('clear')

# 1-task
'''
f = open("/home/ibrohim/Downloads/person's.txt",'r')
em = open('Employed.txt','w')
un = open('Unemployed.txt','w')
p = f.readlines()
for i in p:
    j = i.split(',')[3]
    if j == 'true':
        em.write(i)
    else:
        un.write(i)    
f.close()
em.close()
un.close()
'''
# 2-task
f = open("/home/ibrohim/Downloads/person's.txt",'r')
dc = dict()
p = f.readlines()
for i in p:
    j = i.split(',')[2]
    dc[j] = dc.get(j,0) + 1
print(dc)    
f.close()