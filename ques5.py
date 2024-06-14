#5. Write a program that takes a string input from the user and writes it to a text file.

temp = input("Enter your data: ") 
try: 
    with open('gfg.txt', 'w') as gfg: 
        gfg.write(temp) 
except Exception as e: 
    print("There is a Problem", str(e))