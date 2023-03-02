import random as r
import matplotlib.pyplot as plt
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

plt.plot(x,y,label="array")
print(y)
plt.legend()
plt.show()