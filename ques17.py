#17. Write a program in python that converts a given string to title case (first letter of each word capitalized).
def TC(input_string):
    words = input_string.split()
    title = [word.capitalize() for word in words]
    string1 = ' '.join(title)
    
    return string1
input_string=input("Enter a string: ")
str1 = TC(input_string)
print(str1)