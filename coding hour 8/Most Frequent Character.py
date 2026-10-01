"""
Problem Statement 
Write a program that reads a line of text and finds the letter that appears most often in it. Letters are counted without regard to case, so 'A' and 'a' are the
 same letter, and anything that isn't a letter (digits, spaces, punctuation) is ignored. If two or more letters are tied for the highest count, print the 
 one that comes first in the alphabet. 
 
 Input Format 
 A single line containing the text. 
 
 Output Format 
 Print one line: the most frequent letter in lowercase, a single space, and the number of times it appears. 

"""

text = input("Enter text: ")

text = text.lower()

best_char = ""
best_count = 0

for i in range(97, 123):

    ch = chr(i)
    count = 0

    for c in text:
        if c == ch:
            count += 1

    if count > best_count:
        best_count = count
        best_char = ch

print("Most frequent character:", best_char)
print("Count:", best_count)