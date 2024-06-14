'''21. Write a python program that counts the occurrences of a specific element
in a list'''
lst = []
n = int(input("Enter number of elements : "))
sum=0
for i in range(0, n):
    ele = input("Enter elements: ")
    lst.append(ele)  
x=input("enter the element whoes occurence you want to know: ")
count = 0
for ele in lst:
    if (ele == x):
        count = count + 1
print(x,"occurence in the list",lst,"is",count)