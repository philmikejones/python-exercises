import sys
import os

script, from_file, to_file = sys.argv

print(f"Copying contents of {from_file} to {to_file}...")

if not os.path.exists(to_file):
    print(f"{to_file} does not exist. Creating.")

with open(from_file, "r") as from_file:
    from_file = from_file.read()

with open(to_file, "w") as to_file:
    to_file = to_file.write(from_file)
