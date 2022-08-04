# -*- coding: utf-8 -*-
"""

Compute results of measles testing using simulation and Bayes' Law
 
Instructions: 

  - Problems start with #@ and then give a number.  Enter your
    Python code after each problem.  

  - Your code for a problem can define temporary variables, but
    cannot refer to variables you defined in previous problems
    (unless specifically allowed).

  - If the problem asks you to compute something, the last line
    of your answer must be an *expression* (an expression is
    something that could go on the right hand side of the ' = '
    in an assignment statement)
    
  - Do not use any loops or list comprehensions.
    
Note: Except for the problems where you define a function, the
answers I wrote for all problems are one-liners.

"""

import numpy as np
import pandas as pd

# set the random seed for repeatability
np.random.seed(0)

# Here's an example of how simulate 100 flips of a coin that
# that is weighted 50% towards heads.
flips = np.random.choice(['H', 'T'], 100, p=[0.7, 0.3])
print('100 flips:\n', flips)

#
# Part 1: Simulation
#

# Simulation parameters

# the marginal probability of measles
p_measles  = 0.05
# the probability of a positive test given measles
p_pos_if_measles = 0.90
# the probability of a positive test given no measles
p_pos_if_okay = 0.05
# the total number of people in the simulation
n = 10000

# We will create two boolean NumPy arrays, each containing n boolean values.
# has_measles[i] is True if the ith person has measles
# tests_positive[i] is True if the ith person tests positive for measles

#@ 1
# First we simulate who has measles and who does not.
# Using p_measles, randomly initialize the has_measles array.
# (assignment to has_measles)
has_measles = np.random.choice([True, False], n, p=[p_measles, 1 - p_measles])

# Check the values in has_measles.
# bincount() is similar to Pandas's value_counts(), but for NumPy arrays.
print('Problem 1: ', np.bincount(has_measles))

#@ 2
# Set the value of num_measles to the number of True values in has_measles.
# (assignment to num_measles)
num_measles = has_measles.sum()

# check the answer
print('Problem 2: {}'.format(num_measles))

#@ 3
# Initialize the tests_positive array to all False values
# (assignment to tests_positive)
tests_positive = np.full(n, False)

#@ 4
# Now we simulate, for the people with measles, whether they test
# positive for measles or not.
# Using p_pos_if_measles, randomly initialize the values of 
# tests_positive for people with measles.
# Hint: think about a slightly easier problem: set values in 
# tests_positive to True if they correspond to elements in has_measles
# that are True.
# (update tests_positive)
tests_positive[has_measles] = np.random.choice([True, False], num_measles, p=[p_pos_if_measles, 1 - p_pos_if_measles])

# Check the answer
print('Problem 4: ', np.bincount(tests_positive))

#@ 5
# Now we simulate, for the people without measles, whether they test
# positive for measles or not.
# Using p_pos_if_okay, randomly initialize the values of tests_positive
# for people without measles.
# (update tests_positive)
tests_positive[~has_measles] = np.random.choice([True, False], n - num_measles, p=[p_pos_if_okay, 1 - p_pos_if_okay])

# Compute a confusion matrix using Pandas crosstab()
# use pandas crosstab 
print('Problem 5:\n', pd.crosstab(has_measles, tests_positive))

#@ 6
# Using the has_measles and tests_positive arrays, compute the probability 
# that a person has measles given positive test results.
# (expression)
(has_measles & tests_positive).sum() / tests_positive.sum()

#@ 7
# Using the has_measles and tests_positive arrays, compute the probability 
# that a person has does not have measles given negative test results.
# (expression)
(~has_measles & ~tests_positive).sum() / (~tests_positive).sum()

#@ 8
# Using the has_measles and tests_positive arrays, compute the probability 
# that a person has measles given negative test results.
# (expression)
(has_measles & ~tests_positive).sum() / (~tests_positive).sum()

#@ 9
# Create a data frame with two columns:
# 'measles', which will contain the values in the has_measles array
# 'tests_positive', which will contain the values in the tests_positive array
# (assignment to df)
df = pd.DataFrame({'measles':has_measles , 'tests_positive':tests_positive})

# Create a grouped bar plot showing the number of people with or
# without measles, and the results of their tests.
pd.crosstab(df['measles'], df['tests_positive']).plot.bar()

#@ 10
# Take your answers above and create a function that will perform the simulation
# and return the estimated probability that a person has measles given
# positive test results
# (define a function)
def sim_p_measles_if_pos(p_measles, p_pos_if_measles, p_pos_if_okay):
    n = 10000
    has_measles = np.random.choice([True, False], n, p=[p_measles, 1 - p_measles])
    num_measles = has_measles.sum() 
    tests_positive = np.full(n, False)
    tests_positive[has_measles] = np.random.choice([True, False], num_measles, p=[p_pos_if_measles, 1 - p_pos_if_measles])
    tests_positive[~has_measles] = np.random.choice([True, False], n - num_measles, p=[p_pos_if_okay, 1 - p_pos_if_okay])
    return (has_measles & tests_positive).sum() / tests_positive.sum()

# test the function on the question at the top of the assignment
print('Problem 10: test 1: {:.4f}'.format(sim_p_measles_if_pos(0.01, 0.98, 0.02)))

# test the function on the case where the test is 95% accurate if
# you have measles, and 90% accurate if you don't have measles
print('Problem 10, test 2: {:.4f}'.format(sim_p_measles_if_pos(0.01, 0.95, 0.90)))

#
# Part 2: Bayes' Law
#

#@ 11
# Using Bayes' Law, calculate the probability that a person has measles given
# that their test is positive.
# Use p_measles, p_pos_if_measles, and p_pos_if_okay to compute your answer.
# (expression)
(p_pos_if_measles * p_measles) / ((p_pos_if_measles * p_measles) + (p_pos_if_okay * (1 - p_measles)))

#@ 12
# Take your code that uses Bayes' Law and create a function that will 
# compute the probability that a person has measles given they their
# test is positive.
# (define a function)
def p_measles_if_pos(p_measles, p_pos_if_measles, p_pos_if_okay):
    return (p_pos_if_measles * p_measles) / ((p_pos_if_measles * p_measles) + (p_pos_if_okay * (1 - p_measles)))

# test the function on the question at the top of the assignment
print('Problem 12, test 1: {:.4f}'.format(p_measles_if_pos(0.01, 0.98, 0.02)))

# test the function on another case
print('Problem 12, test 2: {:.4f}'.format(p_measles_if_pos(0.01, 0.95, 0.90)))




