# Write a Python code that takes as input a value n, and generates a list of
# n unique random values. You may use this code to generate the numbers
# to be given as input for the searching and sorting code for the questions
# below.

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


