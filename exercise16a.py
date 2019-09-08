from sys import argv

script, filename = argv

with open(filename, "r") as file:
  print(file.read())
