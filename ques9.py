#9. Write a python program that checks if a substring is present in a given string.
n=input("Enter main string here: ")
n1=input("Eter string you want to check if present here: ")
if n1 in n:
    print(n1,"is a substring of", n)
else:
    print(n1,"is not a substring of", n)