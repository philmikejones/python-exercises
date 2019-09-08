from sys import argv

script, filename = argv

print(f"Truncate (empty) {filename}?")
print("To cancel press CTRL + C (^C)")
print("To delete press RETURN")
input("?")

with open(filename, "w") as file:
    file.truncate()

print(f"{filename} truncated (emptied)")

print(f"Provide 3 lines and they'll be appended to {filename}")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

with open(filename, "w") as file:
    file.write(f"{line1}\n{line2}\n{line3}\n")
