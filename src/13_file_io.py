"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

import os

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file


def read_file(filename):
    try:
        script_directory = os.path.dirname(__file__)

        text_file = open(f"{script_directory}/{filename}", "r")

        content = text_file.read()

        text_file.close()

        return content
    except FileExistsError:
        print(f"{FileNotFoundError}")


print(read_file("foo.txt"))

# YOUR CODE HERE

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# Note: if file does not exist and operation mode is "write"
# it will create the file


def write_to_file(filename, content):
    try:
        script_directory = os.path.dirname(__file__)

        text_file = open(f"{script_directory}/{filename}", "w")

        text_file.write(f"{content}")
        text_file.close()

    except FileNotFoundError:
        print(f"{FileNotFoundError}")


# YOUR CODE HERE
filename = "bar.txt"
content = "This is an example of writting to file"

write_to_file(filename, content)
print(read_file("bar.txt"))
