import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# import csv
df = pd.read_csv('data.csv', header=0)

# newaxis is used to increase the dimension of the existing array by one more dimension
x_train = df['Father'].values[:, np.newaxis]
y_train = df['Son'].values

lm = LinearRegression()

lm.fit(x_train, y_train)

x_test = [[72.8], [61.1], [67.4], [70.2], [75.6], [60.2], [65.3], [59.2]]

predictions = lm.predict(x_test)
print(predictions)

plt.scatter(x_train, y_train, color='b')

plt.plot(x_test, predictions, color='black', linewidth=3)

plt.xlabel('Father height')
plt.ylabel('Son height')
plt.show()
