# -*- coding: utf-8 -*-
"""
NumPy arrays lab.
Enter your code below each comment

@author: Glenn Bruns
"""

import random
import numpy as np

# here is a list of the mileage (given in MPG) of students
# in my last class: 21.1, 26.6, 16.3, 33.7, 31.2, 52.0, 27.1
# create a NumPy array names 'mpg' from these values (use the given order)
mpg = np.array([21.1, 26.6, 16.3, 33.7, 31.2, 52.0, 27.1])
# create a new array x that has the same length as mpg but
# every value is 25.0  (use the NumPy size property of mpg)
x = np.full(mpg.size, 25.0)
# print the mileage of the third student
print(mpg[2])
# print the mileage of the last student
print(mpg[-1])
# print the mileage of the first to the third students
print(mpg[:3])
# print the mileage of every other student, starting with the first
print(mpg[::1])
# can you print the same mileages, but in reverse order?
print(mpg[::-1])
# make a copy of mpg, named mpg2
mpg2 = mpg.copy()
# print the concatenation of mpg and mpg2
np.concatenate([mpg, mpg2])
# print the data type (dtype) of mpg
print(mpg.dtype)
# add 5.0 to every element of mpg2
np.add(mpg2, 5.0)
# create a NumPy array 'miles' giving the distances each
# student has to travel to CSUMB.  The values are:
# 8.1, 5.4, 12.8, 42.1, 15.0, 22.2, 18.5
miles = np.array([8.1, 5.4, 12.8, 42.1, 15.0, 22.2, 18.5])
# the gallons used by a student in a round trip to CSUMB
# is the round-trip distance divided by miles-per-gallon.  Using vectorized
# operations, compute the number of gallons used by each student
# in a round trip to CSUMB.  Assign the result to variable 'gallons'.
gallons = np.divide(miles, mpg)
# create a boolean array that is True for every
# element of gallons that is less than 1.  Assign it to variable 'low_gas'.
low_gas = gallons < 1
# use a boolean mask to get the values in gallons that are less than 1
gallons[gallons < 1]
# run the following line of code, which creates an array of a million
# random numbers between 0 and 1
x = np.array([random.random() for _ in range(10000000)])

# write a python loop to compute the sum of the values in x
#total = 0.0
#for num in x:
#    total += num
# define a Python function named 'array_sum' that will return
# the sum of the specified NumPy array x
def array_sum(x):
    total = 0.0
    for num in x:
        total += num
    return total
# time how long it takes for your function to sum the elements of
# the big array x you defined earlier
# hint: use %timeit in a Jupyter notebook 
# if using .py script, you can use the timeit library as: 
# import timeit
# print(timeit.timeit(lambda: np.sum(x))) 
%timeit array_sum(x)
# now time how long it takes to do the same thing using np.sum
%timeit np.sum(x)
# write code to illustrate that slicing does not copy the input
# data
x = np.arange(5)
print(x)
y = x[2:4]
y[1] = 8
print(x)
# if you still have time, learn about some of the "magic commands"
# available in IPython
# https://ipython.org/ipython-doc/3/interactive/magics.html
