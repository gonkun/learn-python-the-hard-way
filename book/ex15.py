# README
# for run:
# python3.6 ex15.py ex15_sample.txt

# Import module argv from sys
from sys import argv

# unpack arguments o 2 variables 'script' and 'filename'
script, filename = argv

# open file 'filename' and save output ina variable 'txt'
txt = open(filename)

# print string
print(f"Here's your file {filename}:")
# read variable 'txt' and show output
print(txt.read())

print("Type the filename again:")
# insert filename to read again with an input
file_again = input("> ")

# open file again and save it in 'txt_again'
txt_again = open(file_again)


# read value 'txt_again' and print it 
print(txt_again.read())
