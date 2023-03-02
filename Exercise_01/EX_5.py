# as per the basic knowledge in DAA

import random 
import matplotlib.pyplot as plt
def binarySearch_I(array, x, low, high,count):
    while low <= high:
        count+=1
        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def binarySearch_R(array, x, low, high,count):

    if high >= low:
        mid = low + (high - low)//2
        count+=1
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binarySearch_R(array, x, low, mid-1,count)
        else:
            return binarySearch_R(array, x, mid + 1, high,count)
    else:
        return -1
    

n = int(input("Enter your number of elements : "))
final_y_it=[]
final_y_re=[]
final_x = []
for i in range(n):
    arr=[]
    x=[]
    a=0
    while(n!=a):
        r = random.randint(0,1000)
        if r not in arr:
            arr.append(r)
            x.append(a)
            a+=1
    it=0
    re=0
    find_ele = arr[2]
    binarySearch_I(arr, find_ele, 0, len(arr)-1,it)
    final_y_it.append(it)
    binarySearch_R(arr, find_ele, 0, len(arr)-1,re)
    final_y_re.append(re)
    final_x.append(i)

# plt.plot(final_x,final_y_it,lable="Iterative")
# plt.plot(final_x,final_y_re,lable="Recursive")
# plt.legend()

plt.plot(final_x,final_y_it)
plt.plot(final_x,final_y_re)
plt.show()
