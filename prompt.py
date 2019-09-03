import sys

script, user_name = sys.argv
prompt = '> '

print(f"Hi {user_name}, I'm {script}")

age = input(f"How old are you? ")

confirm = input(f"So your name is {user_name} and you're {age} years old? y/n ")

if confirm is "y":
    print("Great")
elif confirm is "n":
    print("Sorry I got something wrong")
    age = input("So what's your correct age? ")
    print(f"So your name is {user_name} and your age is {age}.")
else:
    print("Please confirm retry")
