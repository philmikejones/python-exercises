# Excercise 1
print("Hello World")
print("""Hi this
is a multi-line string
""")

# Excercise 3
# Counting
x = 1 + 3
y = 1 + 3.3
print(type(x))
print(type(y))

print(x > y)

print("The remainder of 13 / 5 is", 13 % 5)
print("The remainder of 13 / 6 is", 13 % 6)

# Excercise 4
cars = 20.0
passengers = 34.0
drivers = 16.0
spaces = cars * 4.0
print("There are", cars, "cars available")
print("There are", passengers, "passengers")
print("There are", drivers, "drivers")

print("There are", cars - drivers, "cars without drivers")
print("There are", spaces, "spaces")
print("There are", spaces - passengers, "unused seats")

# Excercise 5
suit = "Spades"
number = "Ace"

print(f"Your card is the {number} of {suit}")

temperature_c = 19.5
print(f"The temperature in celcius is {temperature_c}")

temperature_f = ((temperature_c * 9) / 5) + 32
print(f"The temperature in farenheit is {temperature_f}")

# Excercise 6
print("This is a string")
f_string = "f-string"
print(f"This is an {f_string}")

format_string = "format string"
print("This is a {}".format(format_string))

# concatenate strings
print(suit + " " + number)

# Exercise 7
print("." * 10)

end1 = "c"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"

# end = " " replaces the new line end with a space
print(end1 + end2 + end3 + end4 + end5 + end6, end = " ")
print("on toast")

# Excercise 8
formatter = "{} {} {} {}"
# .format is a method of the string variable
print(formatter.format(1, 2, 3, 4))
# tuple out of range error if number of strings doesn't match length of
# formatter
print(formatter.format(
    "Cheese",
    "on",
    "toast",
    "biscuits"
))

print(type("This is a string"))
