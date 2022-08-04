# -*- coding: utf-8 -*-
"""
Pandas dataframes

@author: Glenn Bruns
"""

import numpy as np
import pandas as pd


# allow output to span multiple output lines in the console
pd.set_option('display.max_columns', 500)

# =============================================================================
# Read data
# =============================================================================

# read 1994 census summary data
df = pd.read_csv("https://raw.githubusercontent.com/grbruns/cst383/master/1994-census-summary.csv")
df.set_index('usid', inplace=True)
df.drop('fnlwgt', axis=1, inplace=True)

# =============================================================================
# Simple aggregation
# =============================================================================

# print the average age
print(df.age.mean())

# get the mean, max, and avg value for each numeric column
df.describe()
num_cols = df.select_dtypes(include=[np.number]).columns
df[num_cols].agg(['min', 'max', 'mean'])

# for a dataframe you get the aggregate for each column by default
df.mean()

# =============================================================================
# Aggregation with grouping
# =============================================================================

# how many people in each category of education?
# Try using pandas function value_counts().
df['education'].value_counts()

# for each native country, what is the average education num?
df.groupby(['native_country'])['education_num'].mean()

# repeat the previous problem, sorting the output by the average
# education num value
df.groupby(['native_country'])['education_num'].mean().sort_values()

# for each occupation, compute the median age
df.groupby(['occupation'])['age'].median()

# repeat the previous problem, but sort the output
df.groupby(['occupation'])['age'].median().sort_values()

# find average hours_per_week for those with age <= 40, and those with age > 40
df.groupby(df.age > 40)['hours_per_week'].mean()

# do the same, but for age groups < 40, 40-60, and > 60
age_groups = ['<40' if (x < 40) else '>60' if (x > 60) else '40-60' for x in df.age]
df.groupby(age_groups)['hours_per_week'].mean()

# get the rows of the data frame, but only for occupations
# with an average number of education_num > 10
def filter_fun(x):
    return x.education_num.mean() > 10
df_high_ed_occupations = df.groupby('occupation').filter(filter_fun)

# =============================================================================
# Vectorized string operations
# =============================================================================

# create a Pandas series containing the values in the native_country column.
# Name this series 'country'.
country = df.native_country

# how many different values appear in the country series?
country.unique().size

# create a Series containing the unique country names in the series.
# Name this new series 'country_names'.
country_names = pd.Series(country.unique())

# modify country_names so that underscore '_' is replaced
# by a hyphen '-' in every country name.  Use a vectorized operation.
# (See https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html)
country_names = country_names.str.replace('_', '-')

# modify country_names to replace 'Holand' with 'Holland'.
country_names = country_names.str.replace('Holand', 'Holland')

# modify country_names so that any characters after 5 are removed.
# Again, use a vectorized operation
country_names = country_names.str[0:5]

# Suppose we were to use only the first two letters of each country.
# Write some code to determine if any two countries would then share
# a name.
country_names.size == country_names.str[0:2].unique().size

# If you still have time, write code to determine which countries
# do not have a unique name when only the first two characters are
# used.  Hint: look into Pandas' Series.duplicated().
country_names[country_names.str[0:2].duplicated(keep=False)]

# =============================================================================
# Handling times and dates
# =============================================================================

# read gas prices data
gas = pd.read_csv("https://raw.githubusercontent.com/grbruns/cst383/master/Gasoline_Retail_Prices_Weekly_Average_by_Region__Beginning_2007.csv")

# create a datetime series and make it the index of the dataset
gas['Date'] = pd.to_datetime(gas['Date'])
gas.set_index('Date', inplace=True)

# plot the gas prices for NY city
gas[['New York City Average ($/gal)']].plot()

# plot gas prices for NY city and Albany on the same plot
gas[['New York City Average ($/gal)', 'Albany Average ($/gal)']].plot()

# if you still have time, see if you can find and plot California
# gas prices



