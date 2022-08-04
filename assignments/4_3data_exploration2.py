#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 22 19:00:04 2022

@author: katherine vickstrom

"""

import numpy as np
import pandas as pd
from matplotlib import rcParams
import seaborn as sns

sns.set()
sns.set_context('talk')
rcParams['figure.figsize'] = 8,6

# 2.
df = pd.read_csv('https://raw.githubusercontent.com/grbruns/cst383/master/College.csv', index_col=0)

# 3.
# 3.1
sns.scatterplot(x='F.Undergrad', y='Expend', data=df)
sns.regplot(x='F.Undergrad', y='Expend', data=df)

# 3.2
sns.scatterplot(x='F.Undergrad', y='Outstate', data=df)
sns.regplot(x='F.Undergrad', y='Outstate', data=df)

df['F.Undergrad.log'] = df['F.Undergrad'].apply(np.log10)
sns.regplot(x='F.Undergrad.log', y='Outstate', data=df)

# 3.3
df['perc.accept'] = (100.0 * df['Accept'] / df['Apps']).round(0)
df['perc.enroll'] = (100.0 * df['Enroll'] / df['Accept']).round(0)

# at more expensive schools, students are less likely to enroll if accepted
sns.scatterplot(y='perc.enroll', x='Outstate', data=df)
sns.regplot(y='perc.enroll', x='Outstate', data=df)

# more selective schools tend to be more expensive
sns.regplot(y='perc.accept', x='Outstate', data=df)

# More selective schools tend to have lower graduation rates
sns.scatterplot(x='perc.accept', y='Grad.Rate', data=df)
sns.regplot(x='perc.accept', y='Grad.Rate', data=df)
sns.regplot(x='F.Undergrad', y='Grad.Rate', data=df)


# 4.
# it doesn't appear that more selective public schools are more expensive
sns.scatterplot(y='perc.accept', x='Outstate', hue='Private', data=df)

# there is a weak trend showing more expensive public schools are a little more selective
sns.regplot(y='perc.accept', x='Outstate', data=df[df['Private'] == 'No'])
# the trend is stronger among private schools
sns.regplot(y='perc.accept', x='Outstate', data=df[df['Private'] == 'Yes'])

# new categorical variable
breaks = [0,65,80,100]
df['PhD_level'] = pd.cut(df['PhD'], include_lowest=True, bins=breaks, labels=['low', 'medium', 'high'])
sns.scatterplot(y='perc.accept', x='Outstate', style='PhD_level', hue='PhD_level', data=df)
