import random as ran
import time as t
import matplotlib.pyplot as plt
def unique_ele(arr,n):
    array=[]
    i=0
    while i<n:
        if(arr[i] not in array):
            array.append(arr[i])
        i+=1
    return array
n = int(input())
x=[]
y=[]
for i in range(1,n+1):
    a = [ran.randint(0,100) for j in range(i)]
    num = len(a)
    start = t.time()
    arr = unique_ele(a,num)
    end = t.time()
    x.append(i)
    y.append(end-start)
plt.plot(x,y)
plt.show()




