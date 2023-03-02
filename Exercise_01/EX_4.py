# as per the basic knowledge in DAA

import random as r
import matplotlib.pyplot as plt

def insertionSort(arr):
    count=0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
            count+=1
        arr[j + 1] = key
    return count


def shellSort(arr, n):
    count=0
    gap=n//2
    while gap>0:
        j=gap
        while j<n:
            i=j-gap 
            while i>=0:
                if arr[i+gap]>arr[i]:
                    break
                else:
                    arr[i+gap],arr[i]=arr[i],arr[i+gap]
                    
                i=i-gap 
                count+=1
            j+=1
            
        gap=gap//2
    return count

def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


def radixSort(array):
    count=0
    max_element = max(array)
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        count+=1
        place *= 10
    return count
n = int(input("Enter how many times : "))
final_y_insertion=[]
final_y_sell=[]
final_y_radex=[]
final_x=[]
for i in range(n):
    x=[]
    y=[]
    # n  = int(input("Enter the number of element : "))
    a=0
    while(a!=n):
        r1 = r.randint(0,100)
        if r1 not in y:
            y.append(r1)
            x.append(a)
            a+=1
    insertion_sort_list = y
    sell_sort_list = y
    radex_sort_list = y
    final_y_insertion.append(insertionSort(insertion_sort_list))
    final_y_sell.append(shellSort(sell_sort_list,n))
    final_y_radex.append(radixSort(radex_sort_list))
    final_x.append(i)
print("insertion Sort : ",insertion_sort_list)
print("Sell Sort : ",sell_sort_list)
print("radex Sort : ",radex_sort_list)

xx = range(len(final_x))
plt.plot(xx,final_y_insertion,label="Insertion Sort")
plt.plot(xx,final_y_sell,label="Sell Sort")
plt.plot(xx,final_y_insertion,label="Radex Sort")
plt.legend()
plt.show()