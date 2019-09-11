import sys

script, input_file = sys.argv

def print_all(file):
    with open(file, "r") as file:
        print(file.read())

def print_line(file, line):
    line = line - 1
    with open(file, "r") as file:
        for i in range(line):
            file.readline()
        print(file.readline())

print_all(input_file)
print_line(input_file, line = int(input("Which line number would you like to read?: ")))
