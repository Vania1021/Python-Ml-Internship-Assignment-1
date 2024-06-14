#19. Write a python program that removes all punctuation from a given string.
import string
 
my_string = input("ENter a string: ")
new_string = "" 
for char in my_string: 
    if char not in string.punctuation: 
        new_string += char 

print(new_string)