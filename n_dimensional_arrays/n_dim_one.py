import numpy as np

my_array = np.arange(8)     # 8 is stop value

print(my_array)
print(type(my_array))

# What if we wanna start from certain number / 1 instead of 0?
# Then we need to assign 2 parameters.

my_new_array = np.arange(1, 8)

print(my_new_array)

# Lets use only odd numbers, specify 3 arguments
# last argument is step.
my_odd_array = np.arange(1, 8, 2)


my_even_array = np.arange(0, 8, 2)
my_float_array = np.arange(0, 8, 0.5)
print(my_odd_array)
print("Floating point", my_float_array)
print("Floating", type(my_float_array))
print(type(my_odd_array))
print(type(my_even_array))

my_negative_array = np.arange(-10, 20, 3.4)
print(my_negative_array)

# Arrays from lists
from_list = np.array([1, 2, 3])
print("From List to array", from_list)

my_fruit_list = ["apple", "banana", "mango", "cherry",
                 "watermelon", 20, 46]

print(my_fruit_list)

fruit_array = np.array(my_fruit_list)
print(fruit_array)

print("See the memory efficiency of n-dimensional arrays")

print(type(fruit_array[5]))
print(type(from_list[1]))


# Follow this:

from_list_of_array = np.array([1, 2, 3])
print(type(from_list[0]))

print("=======")

from_list_of_array = np.array([1, 2, 3], dtype=np.int8)
print(type(from_list_of_array[0]))