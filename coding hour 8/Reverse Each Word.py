"""
Problem Statement 
Write a program that reads a sentence and reverses the letters of every word while keeping the words themselves in their original order. Words are separated by a 
single space, and any punctuation attached to a word is treated as part of that word and gets reversed with it. For example, "hello world" becomes "olleh dlrow". 

Input Format 
A single line containing the sentence. 

Output Format 
Print one line: the sentence with each word reversed, and the spaces between words left exactly where they were

"""

sentence = input("Enter sentence: ")

answer = ""
word = ""

for ch in sentence:

    if ch == " ":
        answer = answer + word + " "
        word = ""

    else:
        word = ch + word

answer = answer + word

print(answer)