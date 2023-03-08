import random as r
arr=[]
n  = int(input("Enter the number of element : "))
a=0
while(a!=n):
    r1 = r.randint(0,100)
    if r1 not in arr:
        arr.append(r1)
        a+=1
print(arr)


