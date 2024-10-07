import os
os.system("clear")
# 1-task
'''
n = int(input("Enter a number of numbers: "))
i = 0
pro = 1
max_neg = -1000
while i < n:
    num = int(input("Enter a number: "))
    if num % 2:
        pro *= num    
    if(num < 0 and num > max_neg):
        max_neg = num
    i+=1
print("The difference between {} and {} =".format(pro,max_neg),pro-max_neg)
'''
# 2-task
"""
count = 0
while True:
    n = int(input("Enter a number: "))
    if(n == 0):
        break
    if n % 3 == 0 and n % 5 == 0 and n % 7 == 0:
        count += 1
if count < 2:
    print(False)
else:
    print(True)
"""
# 3-task
'''
n = int(input("Enter a number of numbers: "))
i = 0
max_n = 0
while i < n:
    num = int(input("Enter a number: "))
    if num % 11 == 0 and num > max_n:
        max_n = num
    i+=1
if max_n != 0:     
    print(max_n)
else:
    print("There is no such number")
'''
# 4-task
"""
count = 0
while True:
    n = int(input("Enter a number: "))
    if(n == 0):
        break
    if n < 0 and n % 2 == 0:
        count += 1
if count < 3:
    print(False)
else:
    print(True)
"""
# 5-task
'''
n = int(input("Enter a number of numbers: "))
i = 0
min_n = 1000
while i < n:
    num = float(input("Enter a number: "))
    if num > 20 and num < min_n:
        min_n = num
    i+=1
if min_n != 1000:
    print(min_n)
else:
    print("There is no such number")
'''
# 6-task
"""
count = 0
sum_neg = 0
while True:
    n = int(input("Enter a number: "))
    if(n == 0):
        break
    if n % 5 and n % 7:
        count += 1
    if n < 0:
        sum_neg += n
print(count,sum_neg)
"""
# 7-task
'''
n = int(input("Enter a number of numbers: "))
i = 0
count = 0
sum_n = 0
while i < n:
    num = int(input("Enter a number: "))
    if num % 7 == 0:
        count += 1
        sum_n += num
    i+=1
print(sum_n // count)
'''
# 8-task
"""
order = True
num = False
while True:
    n = int(input("Enter a number: "))
    if num == False:
        num = n
        continue
    if(n == 0):
        break
    if n > num:
        order = False
    num = n    
print(order)
"""
# 9-task
'''
count = 0
num = False
while True:
    n = int(input("Enter a number: "))
    if num == False:
        num = n
        continue
    if(n == 0):
        break
    if n >= 0 and num >= 0:
        count += 1
    num = n    
if count < 2:
    print(False)
else:
    print(True)
'''
# 10-task
'''
n = int(input("Enter a number of numbers: "))
i = 0
ex_num,order = False, True
while i < n:
    num = float(input("Enter a number: "))
    if ex_num == False:
        ex_num = num
        i+=1
        continue
    if num < ex_num:
        order = False
    ex_num = num    
    i+=1
print(order)
'''
# 11-task
"""
n = int(input("Enter a number: "))
i = 0
max_neg = False
min_pos = False
while i < n:
    num = float(input("Enter a number: "))
    if max_neg == False and num < 0:
        max_neg = num
        i+=1
        continue
    if min_pos == False and num >= 0:
        min_pos = num
        i+=1
        continue
    if num < 0:
        if num > max_neg:
            max_neg = num
    else:
        if num < min_pos:
            min_pos = num        
    i+=1
print(min_pos-max_neg)
"""
# 12-task
'''
n = int(input("Enter a number: "))
num1, num2, num3 = False, False, False
while n > 0:
    if n % 4 == 0:
        if num1 == False:
            num1 = n
            n-=1
        elif num2 == False:
            num2 = n
            n-=1
        elif num3 == False:
            num3 = n
            n-=1
    n-=1
print("Sum =",num1+num2+num3)
'''
# 13-task
"""
n = 6
i = n
while i >= 0:
    j = i
    while j > 0:
        print("*", end = " ")
        j-=1
    print(end = '\n')
    i-=1
"""
# 14-task
'''
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
num1, num2, num3 = False, False, False
if n1 < n2:
    while n2 > n1:
        if n2 % 5:
            if num1 == False:
                num1 = n2
                n2-=1
            elif num2 == False:
                num2 = n2
                n2-=1
            elif num3 == False:
                num3 = n2
                n2-=1
        n2-=1
else:
    while n1 > n2:
        if n1 % 5:
            if num1 == False:
                num1 = n1
                n1-=1
            elif num2 == False:
                num2 = n1
                n1-=1
            elif num3 == False:
                num3 = n1
                n1-=1        
        n1-=1
print("Sum =",num1*num2*num3)
'''
# 15-task
"""
n = int(input("Enter a number: "))
i = 1
sum_e = 0
while i < n:
    if i % 4 and i % 2 == 0:
        sum_e += i
    i+=1
print("Sum =",sum_e)
"""
# 16-task
'''
i = 20
sum_n = 0
while i < 40:
    if(i % 3 == 0):
        sum_n += i ** 2
    i+=1
print("Result =",sum_n)
'''
# 17-task
i = 20
sum_n = 0
while i < 160:
    if(i % 2 == 0):
        sum_n += i ** 2 
    i+=1
print("Result =",sum_n)