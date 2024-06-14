#20. Write a python program that takes a list of numbers and returns their sum.
lst = []
n = int(input("Enter number of elements : "))
sum=0
for i in range(0, n):
    ele = int(input("Enter numbers: "))
    lst.append(ele)   
    sum=sum+ele
print("Sum of list of numbers",lst,"is",sum)