"""
Problem Statement 
Write a program that reads a base and an exponent and computes base raised to the power exponent — using a loop to multiply, 
not Python's ** operator or the pow() function. 
Input Format 
Two lines, each containing one integer: 
● Line 1: base 
● Line 2: exponent — a non-negative integer 

Output Format 
Print a single integer — base raised to the power exponent. 

"""

base = int(input())  
exp = int(input())  
result = 1  
for i in range(exp):      
    result *= base  
print(result) 