"""Problem Statement 
The k-th triangular number is the sum of every whole number from 1 to k (so the 4th triangular number is 1+2+3+4 = 10). 
Given n, write a program that finds the sum of the first n triangular numbers: T(1) + T(2) + ... + T(n). 
Use two nested for loops — do not use a shortcut formula for either the triangular numbers or their sum.

Input Format 
A single integer, n. 

Output Format 
Print a single integer — the sum T(1) + T(2) + ... + T(n). 
"""

n = int(input())  
total = 0  
for i in range(1, n + 1):  
    triangular = 0  
    for j in range(1, i + 1):  
        triangular += j  
    total += triangular  
print(total) 