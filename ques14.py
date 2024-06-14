#14. Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.
lines = []
while True:
    l = input()
    if l:
        lines.append(l)
    else:
        break;
for l in lines:
    print(l) 
	
