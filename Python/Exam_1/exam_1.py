import os
os.system("clear")

# 2-task
'''
try:
    age = int(input("Enter your age: "))
    print(f"You will be {age+1} next year")
except:
    print('Error occured')
else:
    print('The programme has finished')
'''
# 3-task
"""print([i ** 2 for i in range(10) if i % 2 == 0])"""
# 4-task
'''
def reverser(a):
    if len(a) > 10 and a[0] == 'a':
        return a[::-1]
    elif len(a) < 10 and a[0] == 'b':
        return a

print(reverser(input()))
'''
# 5-task
"""
def words(w:list):
    print('Result:')
    for y in w:
        if 'k' in y or 'K' in y:
            print(y,end = ' ')
ls = list()
n = int(input('Enter a number of words: '))
print(f'Enter {n} words:')
for x in range(n):
    ls.append(input())
words(ls)
"""
# 6-task
'''
alpha = {'a':1,'b':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,
        'r':17,'s':18,'t':19,'u':20,'v':21,'x':22,'y':23,'z':24,"o'":25,"g'":25,'sh':26,'ch':27,'ng':28}
num = {0:'nol',1:'bir',2:'ikki',3:'uch',4:"to'rt",5:'besh',6:'olti',7:'yetti',8:'sakkiz',9:"to'qqiz"}
try:
    n = input("Enter a digit: ")
    print(num.get(int(n)))
except:
    print(alpha.get(n))
'''
# 7-task
"""
dc = {'first_name' : 'John', 'last_name' : 'Doe', 'age' : 34, 'student' : False, 'worker' : True}
f = open('Sample_dictionary','w')
f.write(str(dc))
f.close()
info = open('Sample_dictionary','r')
dt = info.read()
info.close
dt = eval(dt)
print(dt,type(dt))
"""
# 8-task
'''
f = open('Sample_file.txt','w')
text = 'hello world\ntoday is our third exam'
f.write(text)
f.close()

dt = open('Sample_file.txt','r')
words = dt.readlines()
ls = []
for x in words:
    w = x.split(' ')
    ls.extend(w)
ls.sort()
res = ''
for y in ls:
    res += f'{y} '
print(res)
'''