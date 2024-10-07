import os
os.system("clear")

'''
def good_int(n:str)->str:
    s = ''
    for i in range(len(n)-2):
        sub = n[i:i+3]
        if len(set(sub)) == 1:
            if s < sub:
                s = sub
    return s
n = input("Enter a number: ") # 6777133339
print(good_int(n))
'''

"""
st1 = {'oltin', 'olma', 'duo', 'ol'}
st2 = {'olma', 'anor', 'behi', 'uzum', 'nok', 'anjir'}
st1.difference_update(st2)
print(st1)
"""

'''
st1 = {'oltin', 'olma', 'duo', 'ol'}
st2 = {'olma', 'anor', 'behi', 'uzum', 'nok', 'anjir'}
st3 = st2.difference(st1)
print(st3)
'''

"""
st1 = {'oltin', 'olma', 'duo', 'ol'}
st2 = {'olma', 'anor', 'behi', 'uzum', 'nok', 'anjir'}
st3 = st2.symmetric_difference(st1)
print(st3)
"""

'''
st1 = {'olma', 'anor', 'behi', 'uzum', 'banan'}
st2 = {'banan', 'anjir', 'uzum', 'gilos', 'olma', 'behi'}
st1.intersection_update(st2)
print(st1)
'''

"""
st1 = {'olma', 'anor', 'behi', 'uzum', 'banan'}
st2 = {'banan', 'anjir', 'uzum', 'gilos', 'olma', 'behi'}
st3 = st1.intersection(st2)
print(st3)
"""

'''
ls_input = list(map(int,input("Enter the elements: ").split()))
target = int(input('Enter the target: '))
def target_found(ls:list,t:int):
    for x in range(len(ls)):
        for y in range(x+1,len(ls)):
            if ls[x] + ls[y] == t:
                return x,y
print(target_found(ls_input,target))
'''

def roman_numbers(s:str):
    numbers = {'I':1,'V':5,'X':10,'L':50,"C":100,"D":500,"M":1000}
    res = 0
    for i in range(len(s)):
        if i < len(s)-1 and numbers[s[i]] < numbers[s[i+1]]:
            res -= numbers[s[i]]
        else:
            res += numbers[s[i]]
    return res
s = input("Enter a roman number: ")
print(roman_numbers(s))              