# -*- coding: utf-8 -*-
"""Gold Price prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GZhxfxaG9DEjXfBbCc-axVO2fm_AbKf6
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

"""data collection and procesing"""

gold_data = pd.read_csv("gold_data.csv")

gold_data.head()

gold_data.tail()

gold_data.shape

gold_data.info()

"""checking missing values"""

gold_data.isnull().sum()

correlation = gold_data.corr()

plt.figure(figsize=(8,8))
sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, annot_kws={'size': 8}, cmap='Blues')

"""correlation values of GLD"""

print(correlation['GLD'])

"""checking the distribution od GLD"""

sns.displot(gold_data['GLD'], color='green')

X= gold_data.drop(['Date','GLD'], axis =1)
Y = gold_data['GLD']

print(X)

print(Y)

"""splitting into trainning data and testdata"""

X_train,X_test,Y_train,Y_test =train_test_split(X,Y,test_size =0.2, random_state=2)

"""midel trainning"""

regressor = RandomForestRegressor(n_estimators=100)

regressor.fit(X_train,Y_train)

"""model evaluation"""

#prediction on test Data
test_data_predictions = regressor.predict(X_test)

print(test_data_predictions)

# R squared error
error_score = metrics.r2_score(Y_test, test_data_predictions)
print("R suared error: " ,error_score)

"""compare the actual values and predicted values in a Plot"""

# convert to  y_ test to list
Y_test = list(Y_test)

plt.plot(Y_test, color='blue', label="Actual Value")
plt.plot(test_data_predictions,color='green',label='predicted values')
plt.title('Actual Price vs Predicted Values')
plt.xlabel("Number of values")
plt.ylabel("GLD prices")
plt.legend()
plt.show()

