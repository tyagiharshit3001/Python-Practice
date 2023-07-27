import pandas as pd
import matplotlib.pyplot as mpt
from sklearn import model_selection
from sklearn import linear_model

"""
Splitting train-test Datasets:
Using whole dataset for training is not a best practice,
so we divide whole dataset into two sets first is train set and another is test sets.
use sklearn.model_selection.train_test_split() method wit dependent and independent variables as argument and it returns
x_train, x_test, y_train, y_test
"""


df = pd.read_csv('Home_price_testtut.csv')
mpt.xlabel('Area (in Sqft)')
mpt.ylabel('Price ( * 100k)')
mpt.title('Home Price Variance')
mpt.scatter(x=df.area, y=df.price)
mpt.show()
mpt.xlabel('Floors (------>)')
mpt.ylabel('Price (in Rupees)')
mpt.scatter(x=df.floors, y=df.price)
mpt.show()

x = df[['area', 'floors']]
y = df['price']

x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2)

regg = linear_model.LinearRegression()

regg.fit(x_train, y_train)

print(regg.predict(x_test))