#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 22 18:58:46 2022

@author: katherine vickstrom

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams

sns.set()
sns.set_context('talk')   # larger
rcParams['figure.figsize'] = 8,6

# 2.
df = pd.read_csv("https://raw.githubusercontent.com/grbruns/cst383/master/1994-census-summary.csv")

# 4.
df.info()
df.describe()

# 5.
df.drop(columns=['usid', 'fnlwgt'], inplace=True)

# 6.
df.head()

# 7.
df['education_num'].describe()

df['education_num'].plot(kind='hist')
plt.xlabel('years of education')

# 8.
# using histogram
df['education_num'].hist()

# using barplot
df['education_num'].value_counts().plot.bar()  
df['education_num'].value_counts().sort_index().plot.bar()

# 9.
plot = sns.kdeplot(df['capital_gain'], bw_adjust=10)
plt.title('Density of capital gains')
plt.xlabel('Capital gains (US $)')
plot.figure.savefig('capital-gains-density.png')

# 10.
df['workclass'].value_counts()

sns.countplot(y='workclass', data=df)
plt.title('Row counts by work class')

# 11.
(df['sex'].value_counts() / df['sex'].size).plot.bar()
plt.title('Fraction of rows by sex')

# 12.
sns.countplot(y='marital_status', data=df)
plt.title('Row counts by marital status')
plt.ylabel('Marital status')

# 13.
sns.countplot(y='education', data=df, color='darkred')

sns.countplot(y='occupation', data=df, color='darkred')

sns.countplot(y='native_country', data=df)

df['native_country'].value_counts()[:12].apply(np.log10).plot.bar()
plt.title('Row counts by native country')
plt.ylabel('Counts (log10)')
