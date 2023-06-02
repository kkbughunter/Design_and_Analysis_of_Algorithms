# 3. (a) Write a program to print all the most frequently occurring characters
# in a given string, as a list.
# For example, if the input string is “example”,the output should be
# [e]. If the input string is “exist”, then the output should be [e,x,i,s,t].
# (b) What is the complexity of your code

import matplotlib.pyplot as plt
import timeit
def most_frequent_chars1(s):
    max_count = 0
    res = []
    for i in range(len(s)):
        count = 1
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                count += 1
        if count > max_count:
            max_count = count
            res = [s[i]]
        elif count == max_count:
            res.append(s[i])
    return res

def most_frequent_chars2(s):
    freq = {}
    max_count = 0
    res = []
    for c in s:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
        if freq[c] > max_count:
            max_count = freq[c]
            res = [c]
        elif freq[c] == max_count:
            res.append(c)
    return res


x = []
y1 = []
y2 = []
slist = ["example", "ssn cyber security club", "ssn college of engineering"]
for i in range(len(slist)):
    s = slist[i]
    t1 = timeit.timeit(lambda: most_frequent_chars1(s), number=1000)
    t2 = timeit.timeit(lambda: most_frequent_chars2(s), number=1000)
    x.append(i)
    y1.append(t1)
    y2.append(t2)
print(x,y1,y2)
plt.plot(x, y1, label='O(n^2)')
plt.plot(x, y2, label='O(n)')
plt.legend()
plt.xlabel('Input size')
plt.ylabel('Time (seconds)')
plt.show()
