"""
Python provides a number of ways to perform printing. Research
how to print using the print operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the print operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("------using print() with format specifier------")
print("x is %s, y is %s, z is %s" % (x, y, z))
print("-----------------------------------------------\n\n")

# Use the 'format' string method to print the same thing
print("------using format() with placeholder------")
print("x is {}, y is {}, z is {}".format(x, y, z))
print("-----------------------------------------------\n\n")

# Finally, print the same thing using an f-string
print("------using f-string------")
print(f"x is {x}, y is {y}, z is {z}")
print("------------------------------------------")
