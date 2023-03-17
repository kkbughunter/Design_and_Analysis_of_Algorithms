
import random as r
import matplotlib.pyplot as plt
import time as t
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key



def shellSort(array, n):
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2


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
    max_element = max(array)
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10



num = int(input("Enter how many times : "))



final_y_insertion=[]
final_y_sell=[]
final_y_radex=[]

x=[ a for a in range(1,num+1)]
for i in range(1,num+1):
    y=[]
    a=0
    while(a!=i):
        r1 = r.randint(0,100)
        if r1 not in y:
            y.append(r1)
            a+=1
    insertion_sort_list = y
    sell_sort_list = y
    radex_sort_list = y

    start = t.time()
    insertionSort(insertion_sort_list)
    end = t.time()
    final_y_insertion.append(end-start)

    start = t.time()
    shellSort(sell_sort_list,len(y))
    end = t.time()
    final_y_sell.append(end-start)

    start = t.time()
    radixSort(radex_sort_list)
    end = t.time()
    final_y_radex.append(end-start)

plt.plot(x,final_y_insertion,label="Insertion Sort")
plt.plot(x,final_y_sell,label="Sell Sort")
plt.plot(x,final_y_radex,label="Radex Sort")
plt.legend()
plt.show()
