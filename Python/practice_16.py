import os,random
os.system("clear")

def linear_search(target):
    ls = [n for n in range(1,1001)]
    try:
        for i in ls:
            if ls[i] == target:
                return f'{target} is located at the {i}th index'
    except:
        return 'No such number'
# print(linear_search(int(input('Enter a number: '))))

def bubble_sort(ls):
    for x in range(len(ls)):
        for y in range(len(ls)):
            if ls[x] < ls[y]:
                ls[x],ls[y] = ls[y],ls[x]
    return ls
# fruit = ['olma', 'uzum', 'anor', 'nok', 'behi']
# print(bubble_sort(fruit))

def binary_search(ls,target):
    ls.sort()
    beg,end = 0,len(ls)-1
    while beg <= end:
        mid = (beg + end) // 2
        if ls[mid] < target:
            beg = mid + 1
        elif ls[mid] > target:
            end = mid - 1
        else:
            return mid
    return -1
# fruit = ['olma', 'uzum', 'anor', 'nok', 'behi', 'banan', 'shaftoli', 'o\'rik', 'kivi', 'avakado', 'olcha']
# f = input("Enter fruit: ")
# print(f'{f} is located at the {binary_search(fruit,f)}th index')
