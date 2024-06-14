#18. Write a python program that checks if two strings are anagrams of each other
      
         
s1=input("Enter string one: ")
s2=input("Enter string two: ")
if(sorted(s1)== sorted(s2)):
    print("The strings are anagrams.") 
else:
    print("The strings aren't anagrams.")   
