#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 17:04:27 2022

@author: katherine vickstrom

"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from matplotlib import rcParams
import seaborn as sns

sns.set()
sns.set_context('talk')
rcParams['figure.figsize'] = 8,6

# 2.
df = pd.read_csv('https://raw.githubusercontent.com/grbruns/cst383/master/College.csv', index_col=0)

# 3. 
predictors = ['Top10perc', 'F.Undergrad']
X = df[predictors].values

# 4.
target = 'Outstate'
y = df[target].values

# 5.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

# 6.
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 7.
regr = KNeighborsRegressor()
regr.fit(X_train, y_train)

# 8.
predictions = regr.predict(X_test)

# 9.
print(predictions[:10].astype(int))
print(y_test[:10])

# 11.
mse = ((predictions - y_test)**2).mean()
print('MSE: {0:.0f}'.format(mse))

# 12.
mse_blind = ((y_train.mean() - y_test)**2).mean()
print('blind MSE: {0:.0f}'.format(mse_blind))

