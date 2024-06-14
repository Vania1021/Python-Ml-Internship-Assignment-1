'''27. Write a program in python that converts a string into a list of its characters.'''

string = input("Enter thee string: ")
lst = [] 
for letter in string:
    lst.append(letter) 
print(lst)