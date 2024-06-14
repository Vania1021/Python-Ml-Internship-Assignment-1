#12. Write a python program that calculates the sum of the digits of a given number.
n=int(input("Enter a number: "))
sum=0
n1=n
while n>0:
    i=n%10
    sum=sum+i
    n=n//10
print("The sum of the digits of number",n1,"is",sum)