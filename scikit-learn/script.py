# -*- coding: utf-8 -*-
"""
The Program uses the Pima Indian diabetes data set, it is used to check how appropriate it is to be used with the multiple
regression technique. The example on multiple linear regression can be used from scikit-learn concept,
it can be used with this data file (you have to add column labels to the data file, and it is probably easiest if
you save it as a CSV file in Excel with comma as the delimiter). Check the predictions as well as the
“metric root mean squared error Vs mean of the y values” 

@author: amith
"""

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

#from sklearn.cross_validation import train_test_split
#new version of sklearn has train_test_split in model_selection library
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from sklearn import metrics  

#fill up a dataframe with data
dataset = pd.read_csv('pimaSmall.txt')  
print(dataset.shape)
print(dataset.head())
print(dataset.describe())

#prepare the data
#create attributes and labels
#use column names for creating an attribute set and label
x = dataset[['noOfPregrancies','plasma','BP','triceps','insulin','BMI','diabetes',  
       'age']]
y = dataset['coloumn'] 
 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

regressor = LinearRegression()  
regressor.fit(x_train, y_train) 

print()
#the regression model has to find the most optimal coefficients for all the attributes
coeff_df = pd.DataFrame(regressor.coef_, x.columns, columns=['Coefficient'])  
print(coeff_df)

y_pred = regressor.predict(x_test)  
print()
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})  
print(df)
print()
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


