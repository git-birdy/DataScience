#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 23:42:37 2022

@author: katherine vickstrom

data acquisition lab
"""
import pandas as pd
import seaborn as sns
from matplotlib import rcParams

# allow output to span multiple output lines in the console
pd.set_option('display.max_columns', 500)

# switch to seaborn default stylistic parameters
# see the useful https://seaborn.pydata.org/tutorial/aesthetics.html
sns.set()
sns.set_context('paper') # 'talk' for slightly larger

# change default plot size
rcParams['figure.figsize'] = 9,7

# 1. Go to data.gov, and look around a little.  See if you can find a data set
# of interest to you. 

# I found an interesting data set: "National Household Survey on Drug Abuse
# (NHSDA-1995)." It seemed to be very comprehensive with a lot of interesting
# data to explore.

# 2. Look at the icons explaining the format of the data.  Note that often the
# data is in HTML format, meaning a web page is available.  Normally such a web
# page will let a person who is not a data scientist explore the data easily.
# We want the raw data!

# The dataset that I found interesting was a webpage in HTML format. I also
# saw tags for data in CSV, RDF, JSON, and XML format which is what we would
# need as data scientists.

# 3. Go to the following page, which shows various data sets for counties
# around the US:
# https://www.ers.usda.gov/data-products/county-level-data-sets/county-level-data-sets-download-data.aspx

# I went to the page and found a few different data sets for unemployment,
# poverty, education, and population data.

# 4. Download the .xls file for unemployment and median household income for
# the US, states, and counties.

# I downloaded the file.

# 5. Load the data as a pandas data frame.
df = pd.read_excel("/Users/katherine/Downloads/Unemployment.xlsx")

# 6. There is a (slightly older) CSV file for this data on the following github
# page.  Try loading the data set using this URL.
df2 = pd.read_csv("https://raw.githubusercontent.com/grbruns/cst383/master/unemployment.csv")

# 7. How does the work you’re doing with this data to get it into pandas data
# frame relate to the need to have your results be replicable? How would you
# document the source of the data set, and what you did to get it into a format
# that Python can use?

# The work you're doing to get it into a pandas data frame must be replicable
# in order for the results to be reliable. The point of science is that the
# experiemnt must repeatable. I would document the site I pulled the data from
# and the date accessed because it could be chaged over time. I had to import
# the data as a CSV into a Pandas dataframe so that Pythong could use it.

# 8. Data sets often come with associated data dictionaries that explain where
# the data comes from, what the attributes mean, etc.  Where is the
# documentation for this data set?

# All I found was a documentation tab on the site where I accessed the data:
# https://www.ers.usda.gov/data-products/county-level-data-sets/documentation/
