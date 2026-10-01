"""
Problem Statement 
A text-analysis tool needs to break a line of text down by what kind of characters it contains. Write a program that reads one line of text and 
counts how many vowels, consonants, digits, and spaces it has. Vowels are the letters a, e, i, o, u in either uppercase or lowercase. Every other 
letter (including y) counts as a consonant. Punctuation and any other symbols are not counted in any category.

Input Format 
A single line containing the text. 

Output Format 
Print four lines in the exact format: 

"""

text = input("Enter text: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0
others = 0

for ch in text:
    ch = ch.lower()

    if ch in "aeiou":
        vowels += 1

    elif ch.isalpha():
        consonants += 1

    elif ch.isdigit():
        digits += 1

    elif ch == " ":
        spaces += 1

    else:
        others += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Others:", others)