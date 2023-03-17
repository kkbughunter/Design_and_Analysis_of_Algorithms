import random as r
import matplotlib.pyplot as plt

def insertionSort(arr):
	for i in range(1, len(arr)):

		key = arr[i]
		j = i-1
		while j >= 0 and key < arr[j] :
				arr[j + 1] = arr[j]
				j -= 1
		arr[j + 1] = key


def shellSort(arr, n):
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
			j+=1
		gap=gap//2

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


x=[]
y=[]
n  = int(input("Enter the number of element : "))
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

insertionSort(insertion_sort_list)
shellSort(sell_sort_list,n)
radixSort(radex_sort_list)

print("insertion Sort : ",insertion_sort_list)
print("Sell Sort : ",sell_sort_list)
print("radex Sort : ",radex_sort_list)
