import sys

script, user_name, age = sys.argv
prompt = '> '

print(f"Hi {user_name}, I'm {script}")
confirm = input(f"You said you're {age} years old. Is this correct? (y/n) ")

if confirm is "n":
    print("Sorry I got something wrong")
    age = input("So what's your correct age? ")

print(f"""
So your name is {user_name} and you're {age} years old
Great
""")
