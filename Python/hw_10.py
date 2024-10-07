import os, random
os.system('clear')
# 1-function
def isPrime(n:int)-> bool:
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i+=1
    return True
# 2-function
def factorial(n:int)-> int:
    if n != 0:
        return n * factorial(n-1)
    else:
        return 1    
# 3-function
def fibonacci_sequence(n:int)-> list:
    fib = [0,1]
    for i in range(n-2):
        fib.append(fib[-1] + fib[-2])
    return fib
# 4-function
def isPalindrome(s:str)-> bool:
    return s == s[::-1]
# 5-function
def word_count(s:str)-> int:
    s = s.split()
    return len(s)
# 6-function
def temperature_converter(far:float)-> float:
    cel = (far-32) * 5 / 9
    return cel
# 7-function
def bmi_calculator(h:float,w:float)-> float:
    return w / (h * h)
# 8-function
def password_generator(n:int)-> str:
    return ''.join([str(random.randint(1,9)) for i in range(n)])
# 9-function
def average_calculator(ls:list)-> float:
    return sum(ls) / len(ls)
# 10-function
def isValid_date(s:str)-> bool:
    if len(s) != 10:
        return False
    s = s.split('.')
    if len(s[0]) != 2 or len(s[1]) != 2 or len(s[2]) != 4:
        return False
    if int(s[0]) < 1 or int(s[0]) > 31 or int(s[1]) < 1 or int(s[1]) > 12:
        return False
    return True