# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE


def check_even_or_odd(num):
    if num % 2 == 0:
        return f"Number: {num} is even!"
    else:
        return f"Number: {num} is odd!"


# YOUR CODE HERE
# Read a number from the keyboard
num = int(input("Enter a number: "))

# Print out "Even!" if the number is even. Otherwise print "Odd"
print(check_even_or_odd(num))
