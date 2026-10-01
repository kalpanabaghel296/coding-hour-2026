"""
Problem Statement
A teacher wants a quick way to see how a class performed. The passing mark for the exam is 40. Given the marks of n students, 
write a program that counts how many students passed and calculates what percentage of the class that represents, using a for 
loop. 

Input Format 
n + 1 lines of input: 
● Line 1: n — the number of students 
● Next n lines: one integer each — that student's marks (out of 100) 

Output Format 
Print two lines in the exact format: 
"""
n = int(input())  
passed = 0  
for i in range(n):      
    marks = int(input())      
    if marks >= 40:          
        passed += 1  
pct = (passed / n) * 100  
print(f"Passed: {passed}")  
print(f"Pass Percentage: {pct:.2f}%")