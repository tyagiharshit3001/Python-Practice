import pandas as pd
import sklearn
from sklearn import linear_model
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

# import warnings filter
from warnings import simplefilter
# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)

"""
Categorical variables
1. Nominal categorical variable : Do not have any numerical relationship among them.
Example: (Male, female), (green, red, yellow)
2. Ordinal categorical variable : Have numerical relationship among them.
Example: (Graduate, masters, phd) (high, low, medium)

Label Encoding: Method of encoding i.e. converting non-numerical features into numerical features.
                from sklearn.preprocessing import LabelEncoder
                create LabelEncoder object
                obj.fit_transform(feature_name)
                
OneHotEncoding is done for categorical variables by assigning them labels and those labels contains ONE HOT ENCODED BIT

Dummy Variable Trap- Problem of multi-collinearity because of which regression will not run.
Avoidance-  1. By removing constant from regression equation.
            2. For 'n' dummy variables run regression for n-1 dummy variables.
"""

# read csv file
df = pd.read_csv('HomePrice.csv')


# getting dummy variables
df2 = pd.get_dummies(df.bedrooms)

# concatenating dummy variables and dataset
ndf = pd.concat([df, df2], axis="columns")

# removing non depending variables
final = ndf.drop(['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'grade', 'town', 2], axis="columns")

# creating linear reg object
reg1 = linear_model.LinearRegression()
# describing dependent variables
x = final.drop(['price'], axis="columns")
# describing independent
y = final.price
# training model
reg1.fit(x, y)
# using model for prediction
a = reg1.predict([[9760, 1, 0]])

print(a)


# label encoding
"""
le = LabelEncoder()
dlf = df
dlf.town = le.fit_transform(dlf.town)

X = dlf[['town', 'area']].values
Y = dlf.price
ohe = OneHotEncoder(categorical_features=[1])
X = ohe.fit_transform(X).toarray()
X = X[:, 1:]
reg1 = linear_model.LinearRegression()
reg1.fit(X, Y)
b = reg1.predict([[9760, 1, 0]])
"""