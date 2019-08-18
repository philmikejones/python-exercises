# Exercise 13
from sys import argv
script, first, second, third = argv

print(f"The script is called: {script}")
print(f"The first argument is: {first}")
print(f"The second argument is: {second}")
print(f"The third argument is: {third}")

fourth = input("What's the fourth argument? ")

try:
    fourth = int(fourth)
except ValueError:
    print(f"{fourth} is not an integer")

if type(fourth) == int:
    print(f"{fourth} is an integer")

print(type(fourth))
print(f"The fourth argument (with input()) is: {fourth}")
