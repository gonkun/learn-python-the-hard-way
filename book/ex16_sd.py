# README
# for run:
# python3.6 ex16_sd.py <filename>
#
# Exmaple:  python3.6 ex16_sd.py test.txt

# Import 'argv' module from 'sys'
from sys import argv

# Unpack arguments on 2 variables
script, filename = argv

# Print strings
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# Excpect return or CTRL-C for continue or not, using 'input' function
input("?")

print("Opening the file...")
# Using 'open()' module for open a file with mode 'r+' (read and write) and save object inside 'target'.
target = open(filename, 'r+')

print("Truncating the file. Goodbye!")
# Truncate file object
target.truncate()

print("Now I'm going to ask you for three lines.")

# Enter string for write inside opened file line by line.
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# wirite inside file using write() module andpassing strings.
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print(f"This is {filename} content:\n")
# return cursor to begin file
target.seek(0)
# read file object target and print it to putput
print(target.read())


print("And finally, we close it.")
# Close opened file
target.close()
