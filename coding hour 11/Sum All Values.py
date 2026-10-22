"""
Problem Statement 
Store the n expense categories and their amounts in a dictionary, then calculate the total of all the numerical values stored in it 
and print it in the given format. You must add the values yourself using a loop (no built-in sum()).

Input Format 
Line 1: an integer n - number of expense categories. 
Next n lines: a category name (a single word) and an integer amount separated by a space. 

Output Format 
A single line in the format: Total expenses: X where X is the sum of all the amounts.

"""
n = int(input())
expenses = {}

for i in range(n):
    category, amount = input().split()
    expenses[category] = int(amount)

total = 0

for amount in expenses.values():
    total += amount

print("Total expenses:", total)