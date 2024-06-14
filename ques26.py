'''26. Write a program in python that checks if a string starts with a given prefix
or ends with a given suffix.'''
str1=input("Enter any string: ")
x=input("prefix/suffix you want to check: ")
print("is",x,"a prefix of string",str1,"=",str1.startswith(x))
print("is",x,"a suffix of string",str1,"=",str1.endswith(x))

