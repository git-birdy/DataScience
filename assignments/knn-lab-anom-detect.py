# -*- coding: utf-8 -*-
"""

kNN anomaly detection with application to college data

"""

import numpy as np
import pandas as pd
from matplotlib import rcParams
import seaborn as sns
from scipy.stats import zscore

# allow output to span multiple output lines in the console
pd.set_option('display.max_columns', 500)

# switch to seaborn default stylistic parameters
# see the very useful https://seaborn.pydata.org/tutorial/aesthetics.html
sns.set()
sns.set_context('talk')

# change default plot size
rcParams['figure.figsize'] = 10,8

#
# kNN anomaly detector
#

# compute distance between two n-dimensional points
def edist(x,y):
    return np.sqrt(np.sum((x-y)**2))

# return a distance matrix based on columns of float matrix x
def dist(x):
    m = x.shape[0]
    dm = np.zeros((m,m))
    for i in range(m):
        for j in range(i,m):
            dm[i,j] = edist(x[i,:], x[j,:])
            dm[j,i] = dm[i,j]
    return dm

# return indexes of anomalous elements of data frame df
# df - a data frame in which all columns are numeric
# k  - k parameter of KNN
# threshold - number of standard deviations past mean distance
#      to be considered an anomaly
def knn_anomalies(df, k=3, threshold=3):
    # scale the data and compute distance matrix
    x = df.apply(zscore).values
    dm = dist(x)
    
    # Compute and return an array containing the
    # row numbers of data frame df for which the distance to
    # the kth nearest neighbor is more than 'threshold' number
    # of standard deviations above the mean of the distances.
    # Pseudocode:
    # 1. for each row, compute distance to kth neareset neighbor
    # 2. use zscale-normalization on the distances
    # 3. get the indexes of the scaled distances that are larger than threshold
        
    sorted_distances = np.apply_along_axis(np.sort, 1, dm)
    dist_to_k_nearest = sorted_distances[:,k]
    
    dist_std = np.std(dist_to_k_nearest)
    dist_mean = np.mean(dist_to_k_nearest)
    dist_scaled = (dist_to_k_nearest - dist_mean)/dist_std
    
    anomaly_indexes = np.where(dist_scaled > threshold)
    return anomaly_indexes

#
# test the anomaly detector
#
    
# read the college data
df = pd.read_csv('https://raw.githubusercontent.com/grbruns/cst383/master/College.csv', index_col=0) 

# compute the anomalies
features = ['Outstate', 'F.Undergrad']
anoms = knn_anomalies(df[features], k=7, threshold=6)

# add new 'Anomaly' column
x = np.full(len(df), False)
x[anoms] = True
df['Anomaly'] = x

# plot the colleges, showing anomalies
sns.scatterplot('Outstate', 'F.Undergrad', data=df, hue='Anomaly', style='Private')
