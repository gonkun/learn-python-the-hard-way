# Import argv from module 'sys'
from sys import argv

# Split parameters to each variable
script, input_file = argv


# Create function 'print_all' passing argument 'f'. f will be a file
def print_all(f):
    # Print output result read the file 'f'
    print(f.read())


# Create funciton 'rewind' passing a file 'f'
def rewind(f):
    # Move cursor to first lines of file
    f.seek(0)


# Create function print_a_line passing 2 arguments:
# number of line toread and a file
def print_a_line(line_count, f):
    # Print numberof line and its content
    print(line_count, f.readline())

# Store on variable 'current_file' the file opened
current_file = open(input_file)

print("First let's print the whole file:\n")

# Call function 'print_all' passing opened file
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# Call 'rewind' function passing opened file
rewind(current_file)

print("Let's print three lines:")

# Set number of line to 1
current_line = 1
# Call function 'print_a_line'
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
