import os
os.system('clear')
os.chdir("/home/ibrohim/Files_py")
'''
s = '123'
n = list(map(str,s))
num = int("".join(n))
print(num)
'''
"""
x = 42
print('no') if x > 42 else print('yes') if x == 42 else print("maybe")
"""
'''
def plus_one(ls:list)-> list:
    n = int(''.join(map(str,digits))) + 1
    return [int(x) for x in str(n)]
digits = list(map(str,input('Enter the digits: ').split()))
print(plus_one(digits))
'''
"""
s,ls = input('Enter a string: '), []
change_letters = lambda x: x[-1] + x[1:-1] + x[0]
for x in s.split():
    ls.append(change_letters(x))
s = ' '.join(map(str,ls))
print(s)
"""
'''
dc = {"A":0,"B":1,"C":2,"D":3,"E":4}
f = open('dictionary.txt',"w+")
f.write(str(dc))
f.seek(0)
res = f.read()
print(res)
'''
"""
s = input("Enter a string: ") # 2+3*5-2+9/(2+7/5-123)
pls = s.count('+')
mns = s.count('-')
mltpl = s.count('*')
dvd = s.count('/')
mdls = s.count('%')
prnthss_l = s.count('(')
prnthss_r = s.count(')')
prnthss = prnthss_l if prnthss_l == prnthss_r else 'Parenthesis error'
print(f'+ : {pls}\n- : {mns}\n* : {mltpl}\n/ : {dvd}\n% : {mdls}\n() : {prnthss}')
"""
