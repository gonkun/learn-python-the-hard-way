cars = 140  # number of cars
space_in_a_car = 4  # space ona car
drivers = 30  # number of drivers
passengers = 90  # number of passengers
cars_not_driven = cars - drivers  # cars without drivers
cars_driven = drivers  # cars with a driver
# people that can we have transport with free cars
carpool_capacity = cars_driven * space_in_a_car
# average passengers that a car can bring
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
