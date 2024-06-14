'''24. Write a program that acts as a simple calculator. It should take two
numbers and an operator (+, -, *, /) as input and print the result.'''
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
n3=input("Enter operation you want to perform(+,-,*,/): ")
if n3=='+' :
    print("sum of both the numbers",n1,"and",n2,"is",n1+n2)

if n3=='-' :
    print("difference of both the numbers",n1,"and",n2,"is",n1-n2)
    
if n3=='*' :
    print("product of both the numbers",n1,"and",n2,"is",n1*n2)

else :
    print("division of both the numbers",n1,"and",n2,"is",n1/n2)



