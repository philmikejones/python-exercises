# import argv function from sys module
from sys import argv

# specify script and filename from command line when calling script
script, filename = argv

# open connection to and read file
with open(filename, "r") as file:
  file = file.read()

# print out file contents
print(file)
