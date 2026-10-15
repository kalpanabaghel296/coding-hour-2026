"""
Problem Statement 
Write a program that reads a sentence and reports two things: how many words it contains, and the length of the longest word in it. 
Words are separated by single spaces. 

Input Format 
A single line containing the sentence. 

Output Format 
Print two lines in the exact format: 

"""

sentence = input()  
word_count = 1  
current_len = 0  
longest = 0  
for ch in sentence:      
    if ch == " ":          
        word_count += 1          
        current_len = 0      
    else:          
        current_len += 1          
        if current_len > longest:              
            longest = current_len  
print("Words:", word_count)  
print("Longest Word Length:", longest) 