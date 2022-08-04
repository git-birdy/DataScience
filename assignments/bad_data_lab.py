#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 22 17:50:04 2022

@author: katherine vickstrom

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# allow output to span multiple output lines in the console
pd.set_option('display.max_columns', 500)

# switch to seaborn default stylistic parameters
# see the useful https://seaborn.pydata.org/tutorial/aesthetics.html
sns.set()
sns.set_context('paper') # 'talk' for slightly larger

# 1.
infile = 'https://raw.githubusercontent.com/grbruns/cst383/master/campaign-ca-2016-sample.csv'
df = pd.read_csv(infile)

# 3.
df.info()
# There are two columns that are numeric, I'm not sure if there's any non
# numeric columns that should be numeric

# 4. 
df.isna().sum()        
df.isna().sum().sum()

# 5.


# 6 & 7.
df['contbr_employer'].value_counts().head(n=20)
# There is misssing data because some are marked as none. Other issues are that
# the same thing will be written different and therefore counted different. Eg.
# "self employed" vs "self-employed" and this should be changed.

# 8. 
# number of different values in memo_cd
len(df['memo_cd'].unique())
# values of memo_cd
df['memo_cd'].value_counts()
# fraction of values that are empty
df['memo_cd'].isnull().mean()

# 9. 
sns.distplot(df['contb_receipt_amt'])
plt.title('Histogram of contribution amounts')
plt.xlabel('Contribution amount (US dollars)')
plt.ylabel('Count')

# 10.
df.describe()
# the min is suspicious because it's negative
df_neg = df[df['contb_receipt_amt'] < 0][['contbr_nm', 'contb_receipt_amt']]
df_neg['contb_receipt_amt'].value_counts()
# negative values don't correlate to positive values
temp = df[df['contb_receipt_amt'].abs() == 2700.0][['contbr_nm', 'contb_receipt_amt']]
temp['contb_receipt_amt'].value_counts()

# 11.
df['contbr_zip'].str.len().value_counts()
# I think the zipcode data would have to be in the same format which it's not.

# 12.
df['contbr_employer'].str.len().hist()
# by looking at the data it seems shorter length for employer names is due to
# many people having "self" as employer as well as employers that have names
# which are acronyms.