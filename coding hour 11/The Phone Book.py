"""
Problem Statement 
Store n contacts, then answer q queries. For each query name, print the phone number, or Not Found if the name does not exist in the 
phone book. 

Input Format 
Line 1: two integers n and q. Next n lines: a name and a phone number separated by a space. 
Next q lines: one query name per line. 

Output Format 
For each query print one line - the phone number or Not Found

"""
n, q = map(int, input().split())

phonebook = {}

for i in range(n):
    name, number = input().split()
    phonebook[name] = number

for i in range(q):
    name = input()
    if name in phonebook:
        print(phonebook[name])
    else:
        print("Not Found")