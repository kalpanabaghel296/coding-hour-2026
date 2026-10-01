"""
Problem Statement Easy Priya decides to start a savings habit. She saves a fixed amount in the first month, 
and increases her savings by a fixed amount every month after that. Given her starting saving amount, the monthly increment, 
and the number of months, write a program to find her total savings using a for loop. 

Input Format 
Three lines, each containing one integer: 
● Line 1: start — the amount saved in month 1 
● Line 2: increment — how much more she saves each following month 
● Line 3: months — the number of months to track 

Output Format 
Print a single integer — her total savings across all the months.

"""
start = int(input())  
increment = int(input())  
months = int(input())  
total = 0  
current = start  
for i in range(months):  
    total += current  
    current += increment  
print(total) 