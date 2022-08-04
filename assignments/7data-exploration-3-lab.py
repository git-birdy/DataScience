import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sns

sns.set()
sns.set_context('talk')  
rcParams['figure.figsize'] = 8,6

# 2.
df = pd.read_csv('https://raw.githubusercontent.com/grbruns/cst383/master/College.csv', index_col=0)

# 3.
breaks = df['F.Undergrad'].quantile([0,0.33, 0.66, 1.0])
df['Size'] = pd.cut(df['F.Undergrad'], include_lowest=True, bins=breaks, labels=['small', 'medium', 'large'])

df.Size.value_counts().plot.bar()

# 4.
g = sns.FacetGrid(df, col='Size', height=4, aspect=0.8)
g.map(plt.scatter, 'PhD', 'Outstate', s=20, color="r")

# 5.
sns.scatterplot(x='PhD', y='Outstate', hue='Size', data=df, s=50)

# 6.
sns.scatterplot(x='PhD', y='Outstate', hue='Size', style='Size', data=df, s=55)

# 7.
sns.catplot(y='Outstate', col='Size', data=df, kind='violin', height=4, aspect=0.7)

# 8.
sns.catplot(y='Outstate', col='Size', data=df, kind='violin', inner='stick', height=4, aspect=0.7)