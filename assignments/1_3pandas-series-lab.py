# -*- coding: utf-8 -*-
"""
Pandas series lab

@author: Glenn Bruns
"""

import numpy as np
import pandas as pd

# here are the MPG values for 7 students in a NumPy array
student_mileage = [21.1, 26.6, 16.3, 33.7, 31.2, 52.0, 27.1]

# here are the names of the seven students
students = ['Sean', 'Laura', 'Angel', 'Mariana', 'Austin', 'Jose', 'Ana']

# create a Pandas series containing the MPG values, using the
# names for the index.  Use variable 'mpg'
mpg = pd.Series(student_mileage, index=students)
# print the series you just created
print(mpg)
# print the mileage for Ana's car using dictionary-style indexing
print(mpg["Ana"])
# print the mileage for Mariana's car using 'loc'
print(mpg.loc["Mariana"])
# print the mpg values that are greater than 30.0
# hint: use a boolean mask
print(mpg[mpg > 30])
# create a series high_mpg that contains the mpg values
# greater than 30.0
high_mpg = mpg[mpg > 30]
# print the high_mpg series
print(high_mpg)
# print the names of the students who have cars with mpg
# greater than 30.0.  
# hint: what's in the index of high_mpg?
print(high_mpg.index)
# create a NumPy array x from the data values in series mpg
x = high_mpg.values
# write code to make sure that x is really a numpy array,
# and not just a Python list
type(x)
# here are the distances that students have to travel (one-way)
# to get to CSUMB
student_dist = {'Sean':8.1, 'Laura':5.4, 'Angel':12.8, 'Austin':15.0, 'Jose':22.2, 'Ana':18.5}

# create a Pandas series 'distance' that gives the distance for each student
distance = pd.Series(student_dist)
# create a series 'rt_distance' from 'distance' that gives the round-trip distance
# hint: use a vectorized operation
rt_distance = distance * 2
# write code to see if the rt_distance series, and the mpg series, mention
# the same students
# hint: index objects support an 'equals' method
rt_distance.index.equals(mpg.index)
# compute the gallons used in each CSUMB commute for each student by 
# dividing the round-trip distance values by the mpg values
rt_distance / mpg
# repeat your calculation, but now give a value of 0 for students that
# students not represented in the mpg or rt_distance time series
rt_distance.divide(mpg, fill_value=0.0)
# If you still have time, play more with some Pandas series
# to get comfortable with indexing.  Also, play with other
# series features discussed in lecture.

# Also, check out this "10 Minutes to pandas" tutorial:
# https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html
