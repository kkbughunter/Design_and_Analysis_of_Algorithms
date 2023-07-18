# Design_and_Analysis_of_Algorithms
The design and analysis of algorithms is a field of computer science that involves the study of algorithms as tools for problem-solving. 

## install necessary packages in python3
This commands for Windows users
```commands:
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  python get-pip.py
  pip install matplotlib 
```

This commands for Linux users
```command:
  sudo apt install python
  sudo apt install python3-pip
  pip install matplotlib 
```
## Exercise
1. [Exercise-1](https://github.com/KKBUGHUNTER/Design_and_Analysis_of_Algorithms/tree/main/Exercise_01) Searching and Sorting <br>


| Algorithm               | Best Case          | Average Case       | Worst Case        | Recurrence Equation         |
|-------------------------|--------------------|--------------------|-------------------|-----------------------------|
| Unique Elements         | O(n)               | O(n)               | O(n log n)        | -                           |
| Tower of Hanoi          | O(2^n)             | O(2^n)             | O(2^n)            | T(n) = 2T(n-1) + 1           |
| Fibonacci               | O(1)               | O(2^n)             | O(2^n)            | F(n) = F(n-1) + F(n-2)       |
| Factorial               | O(n)               | O(n)               | O(n)              | -                           |
| Matrix Multiplication   | O(n^3)             | O(n^3)             | O(n^3)            | -                           |
| Polynomial Evaluation   | O(n)               | O(n)               | O(n)              | -                           |
| Primality Checking      | O(sqrt(n))         | O(sqrt(n))         | O(sqrt(n))        | -                           |
| GCD of Two Numbers      | O(log(min(a,b)))   | O(log(min(a,b)))   | O(log(min(a,b)))  | -                           |
| Binary Search           | O(1)               | O(log n)           | O(log n)          | -                           |
| Linear Search           | O(1)               | O(n)               | O(n)              | -                           |
| Interpolation Search    | O(1)               | O(log log n)       | O(n)              | -                           |
| Selection Sort          | O(n^2)             | O(n^2)             | O(n^2)            | -                           |
| Bubble Sort             | O(n)               | O(n^2)             | O(n^2)            | -                           |
| Insertion Sort          | O(n)               | O(n^2)             | O(n^2)            | -                           |
| Merge Sort              | O(n log n)         | O(n log n)         | O(n log n)        | T(n) = 2T(n/2) + O(n)        |
| Quick Sort              | O(n log n)         | O(n log n)         | O(n^2)            | T(n) = T(k) + T(n-k-1) + O(n)|
| Radix Sort              | O(kn)              | O(kn)              | O(kn)             | -                           |
| Karatsuba Multiplication       | O(n^log2(3))            | O(n^log2(3))            | O(n^log2(3))           | T(n) = 3T(n/2) + O(n)         |
| Largest Integer Multiplication | O(n)                    | O(n)                    | O(n)                   | -                              |
| Matrix Multiplication          | O(n^3)                  | O(n^3)                  | O(n^3)                 | -                              |
| Strassen's Matrix Multiplication | O(n^log2(7))           | O(n^log2(7))           | O(n^log2(7))          | T(n) = 7T(n/2) + O(n^2)       |



| Algorithm                       | Best Case         | Average Case      | Worst Case         | Recurrence Equation  |
|---------------------------------|-------------------|-------------------|--------------------|----------------------|
| Primality Checking              | O(1)              | O(√n)             | O(√n)              | -                    |
| Counting Inversions             | O(n log n)        | O(n log n)        | O(n^2)             | -                    |
| GCD of Two numbers              | O(log min(a, b))  | O(log min(a, b))  | O(log min(a, b))   | -                    |
| Fibonacci                       | O(1)              | O(1.618^n)        | O(1.618^n)         | -                    |
| Towers of Hanoi                 | O(2^n)            | O(2^n)            | O(2^n)             | -                    |
| Bubble Sort                     | O(n)              | O(n^2)            | O(n^2)             | T(n) = T(n-1) + O(n) |
| Selection Sort                  | O(n^2)            | O(n^2)            | O(n^2)             | T(n) = T(n-1) + O(n) |
| Unique Elements                 | O(n)              | O(n)              | O(n log n)         | -                    |
| Sum of series                   | O(1)              | O(n)              | O(n)               | -                    |
| Frequent occurring alphabet     | O(n)              | O(n)              | O(n)               | -                    |
| Binary Search                   | O(1)              | O(log n)          | O(log n)           | T(n) = T(n/2) + O(1) |
| Interpolation Search            | O(1)              | O(log log n)      | O(n)               | -                    |
| Polynomial Evaluation           | O(n)              | O(n)              | O(n^2)             | -                    |
| Karatsuba Algorithm             | O(n^log2(3))      | O(n^log2(3))      | O(n^log2(3))       | -                    |
| Loop Invariant                  | O(1)              | O(n)              | O(n)               | -                    |
| Binomial Coefficient            | O(k)              | O(k)              | O(k)               | -                    |
| Matrix Chain Multiplication     | O(n^3)            | O(n^3)            | O(n^3)             | -                    |
| Knapsack                        | O(nW)             | O(nW)             | O(nW)              | -                    |
| Kth smallest element            | O(n)              | O(n)              | O(n^2)             | -                    |
| LCS Algorithm                   | O(nm)             | O(nm)             | O(nm)              | -                    |
| LCS_DP                          | O(nm)             | O(nm)             | O(nm)              | -                    |
| Sieve of Eratosthenes           | O(n log log n)    | O(n log log n)    | O(n log log n)     | -                    |
| Exponentiation (a^b mod n)      | O(log b)          | O(log b)          | O(log b)           | -                    |
| Prim's Algorithm                | O(E log V)        | O(E log V)        | O(E log V)         | -                    |
| Coin Change                     | O(coins * amount) | O(coins * amount) | O(coins * amount)  | -                    |
| DFS                             | O(V + E)          | O(V + E)          | O(V + E)           | -                    |
| BFS                             | O(V + E)          | O(V + E)          | O(V + E)           | -                    |
| Floyd's Algorithm               | O(V^3)            | O(V^3)            | O(V^3)             | -                    |
| Transitive Closure              | O(V^3)            | O(V^3)            | O(V^3)             | -                    |
| Kruskal's Algorithm             | O(E log V)        | O(E log V)        | O(E log V)         | -                    |
| Longest Palindromic Subsequence | O(n^2)            | O(n^2)            | O(n^2)             | -                    |
| Bubble Sort                     | O(n)              | O(n^2)            | O(n^2)             | T(n) = T(n-1) + O(n) |
| Selection Sort                  | O(n^2)            | O(n^2)            | O(n^2)             | T(n) = T(n-1) + O(n) |
| Insertion Sort                  | O(n)              | O(n^2)            | O(n^2)             | T(n) = T(n-1) + O(n) |
| Merge Sort                      | O(n log n)        | O(n log n)        | O(n log n)         | -                    |
| Binary Search                   | O(1)              | O(log n)          | O(log n)           | T(n) = T(n/2) + O(1) |
| Selection Search                | O(n)              | O(n^2)            | O(n^2)             | T(n) = T(n-1) + O(n) |
| Interpolation Search            | O(1)              | O(log log n)      | O(n)               | -                    |
| Quick Sort                      | O(n log n)        | O(n log n)        | O(n^2)             | T(n) = T(n-1) + O(n) |
