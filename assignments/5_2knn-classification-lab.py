import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# 2.
df = pd.read_csv('https://raw.githubusercontent.com/grbruns/cst383/master/College.csv',index_col=0)

# 3.
df.info()
df.describe()

# 4.
X = df[['Outstate', 'F.Undergrad']].values
y = (df['Private'] == 'Yes').values.astype(int) # Private = 1
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test  = scaler.transform(X_test)

# 5.
print(X_train[:10,:])

# 6.
clf = KNeighborsClassifier()
clf.fit(X_train, y_train)

# 7.
predictions = clf.predict(X_test)

# 8.
print(predictions[:10])
print(y_test[:10])

# 10.
accuracy = (predictions == y_test).mean()
print('accuracy: {0:.3f}'. format(accuracy))
