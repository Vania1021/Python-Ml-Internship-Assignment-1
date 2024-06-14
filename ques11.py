#11. Write a python program that generates the first n numbers in the Fibonacci sequence.
#finbonacci series is like
#0 1 1 2 3 5 8... 
#where each number is sum of first two numbers 
n=int(input("Enter how many numbers you want in fibonacci series: "))
num1 = 0
num2 = 1
next_number = num2  
count = 1
print(num1,end=" ") 
print(num2,end=" ") 
while count <= n-2:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
print()
