"""
Problem Statement 
Write a program that reads two positive integers and finds their GCD (Greatest Common Divisor) and LCM (Least Common Multiple). 
Find the GCD using the Euclidean algorithm: repeatedly replace the larger number with the remainder of dividing the larger by the 
smaller, until the remainder is 0 — the last non-zero value is the GCD. Once you have the GCD, the LCM follows directly from the 
relationship (a × b) = GCD × LCM. 

Input Format 
Two lines, each containing one integer: 
● Line 1: a 
● Line 2: b 

Output Format 
Print two lines in the exact format: 

"""
a = int(input())  
b = int(input())  
x = a  
y = b  
while y != 0:      
    x, y = y, x % y  
    gcd = x  
    lcm = (a * b) // gcd  
print("GCD:", gcd)  
print("LCM:", lcm) 