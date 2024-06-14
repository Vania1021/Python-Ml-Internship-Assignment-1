#13. Write a program that asks the user for their birth year and calculates their age.
from datetime import date
n=int(input("Enter your birth year: "))
current = date.today()
year = current.year
print("Your age is",year-n)
