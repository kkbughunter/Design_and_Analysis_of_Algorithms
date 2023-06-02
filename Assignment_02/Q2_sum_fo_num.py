# a) Given an integer n as input, write a program to print the sum of the
# following series up to n terms.
# 1 + (1 + 2) + (1 + 2 + 3) + . . . + (1 + 2 + 3 + . . . + n)
# (b) What is the time complexity of your code?
import time as t
import matplotlib.pyplot as plt


def sum_of_n(arr):
    sum=0
    for i in range(len(arr)):
        sum +=sum
    return sum

n = int(input("Enter the number of "))
x = []
y1 = []
y2 = []
for i in range(1, n + 1):
    a = [j for j in range(i)]

    start = t.time()
    arr = sum_of_n(a)
    end = t.time()
    x.append(i)
    y1.append(end - start)
    
    start = t.time()
    arr = i*(i+1)/2
    end = t.time()
    y2.append(end - start)
    
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()
