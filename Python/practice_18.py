import os
from heapq import *
os.system('clear')

def toHeap(arr,n,i):
    largest = i
    l,r = 2 * i + 1, 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        toHeap(arr,n,largest)

'''ls = [2,1,4,5,8,7]
# 1-task
heapify(ls)
print(ls)
# 2-task
for i in range(len(ls) // 2 - 1, -1, -1):
    toHeap(ls,len(ls),i)
print(ls)'''

'''hp = [1,2,3,4,6,7]
heapify(hp)
# 3-task
for i in [5,8,9,10,11]:
    heappush(hp,i)
print(hp)
# 4-task
for i in range(6):
    heappop(hp)
print(hp)'''

'''ls = [_ for _ in range(1,11)]
# 5-task
heapify(ls)
print(ls)
print(nsmallest(3,ls))
# 6-task
for i in range(len(ls) // 2 - 1, -1, -1):
    toHeap(ls,len(ls),i)
print(ls)
print(nlargest(5,ls))
# 7-task
heapify(ls)
print(ls)
for j in range(11,25):
    heappush(ls,j)
print(heappushpop(ls,25))
print(ls)
# 8-task
heapify(ls)
print(ls)
print(heappop(ls))
for j in range(25,37):
    heappush(ls,j)
print(ls)
print(len(ls))'''