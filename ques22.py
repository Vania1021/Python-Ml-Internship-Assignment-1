'''22. Write a python program that returns the minimum and maximum values
in a list of numbers.'''
lst = []
n = int(input("Enter number of elements : "))
sum=0
for i in range(0, n):
    ele = int(input("Enter numbers: "))
    lst.append(ele)   
lst.sort()
print("the minimum element is",lst[0])
print("the maximum element is",lst[-1])



