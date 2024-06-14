#6. Write a program that reads the content of a text file and prints it to the console.
def read_file(filename):
  with open(filename, "r") as f:
    file_content = f.read()
  return file_content


def main():
  filename = input("Enter the name of the file to read: ")
  file_content = read_file(filename)
  print(file_content)


if __name__ == "__main__":
  main()
