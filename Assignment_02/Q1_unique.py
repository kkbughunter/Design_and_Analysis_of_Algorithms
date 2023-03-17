import random as ran
import time as t
import matplotlib.pyplot as plt


def unique_ele(arr, n):
    array = []
    i = 0
    while i < n:
        if (arr[i] not in array):
            array.append(arr[i])
        i += 1
    return array


n = int(input())
x = []
y1 = []
y2 = []
for i in range(1, n + 1):
    a = [ran.randint(0, 100) for j in range(i)]
    num = len(a)

    start = t.time()
    arr = unique_ele(a, num)
    end = t.time()
    x.append(i)
    y1.append(end - start)
    
    start = t.time()
    arr = set(a)
    end = t.time()
    y2.append(end - start)
    
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()
