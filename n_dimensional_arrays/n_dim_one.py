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
