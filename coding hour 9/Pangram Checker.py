"""
Problem Statement 
A pangram is a sentence that uses every letter of the alphabet (a to z) at least once. 
"The quick brown fox jumps over the lazy dog" is a famous example. Write a program that reads a line of text and checks whether 
it is a pangram, ignoring case. 

Input Format 
A single line containing the text. 

Output Format 
Print "Pangram" if every letter a–z appears at least once in the text, otherwise print "Not a Pangram".

"""
text = input().lower()  
found_all = True  
for code in range(97, 123):  
    letter = chr(code)  
    present = False  
    for ch in text:  
        if ch == letter:  
            present = True  
            break  
    if not present:  
        found_all = False  
        break  
if found_all:  
    print("Pangram")  
else:  
    print("Not a Pangram")