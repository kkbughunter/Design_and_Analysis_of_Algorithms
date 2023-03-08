import random 
import matplotlib.pyplot as plt
import time as t


def binary_search_I(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0 
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

def binary_search_R(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search_R(arr, low, mid - 1, x)
        else:
            return binary_search_R(arr, mid + 1, high, x)
    else:
        return -1
n = int(input("Enter your number of elements : "))
final_y_it=[]
final_y_re=[]
final_x = [a for a in range(1,n+1)]
for i in range(1,n+1):
    arr=[]
    a=0
    while(n!=a):
        r = random.randint(0,1000)
        if r not in arr:
            arr.append(r)
            a+=1
    find_ele = arr[2]

    start = t.time()
    binary_search_I(arr, find_ele)
    end = t.time()
    final_y_it.append(end-start)

    start = t.time()
    binary_search_R(arr,  0, len(arr)-1, find_ele)
    end = t.time()
    final_y_re.append(end-start)

plt.plot(final_x,final_y_it,label="Iterative")
plt.plot(final_x,final_y_re, label="Iterative")
plt.legend()
plt.show()
