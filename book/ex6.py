# Set variable types_of_people
types_of_people = 10
# Set variable string 'x' with another string inside
x = f"There are {types_of_people} types of people."

# Set more strings on variables
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# Print variables x and y
print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

# Set a boolean on 'hilarious'
hilarious = False
# Set a string on 'joke_evaluation'
joke_evaluation = "Isn't that joke so funny?! {}"

# Print variable 'joke_evaluation' using function .format() for print 'hilarious' variable
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."


# Concat 2 variable swith strings.
print(w + e)
