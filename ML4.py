import pandas as pd
import matplotlib.pyplot as mpt
from sklearn import model_selection
from sklearn import linear_model
import numpy as np

"""
Logistic regression is a regression used for categorical prediction that is boolean prediction.
It uses Sigmoid function:
σ(x) = (1/(1+e^(-x))) which converts:
(ꝏ <= x <= ꝏ) => (0 <= σ(x) <= 1) 
"""

"""
df = pd.read_csv('Insurance.csv')
mpt.title('Insurance details')
mpt.xlabel('Age (in years)')
mpt.ylabel('Insured (Bool values)')
mpt.scatter(x=df.Age, y=df.Insured)
mpt.show()

x_train, x_test, y_train, y_test = model_selection.train_test_split(df[['Age']], df['Insured'], test_size=0.1)

logreg = linear_model.LogisticRegression()

logreg.fit(x_train, y_train)

logreg.predict(x_test)

"""


"""

Exercise: For data set: HR_comma_sep.csv 
1. Now do some exploratory data analysis(EDA) to figure out which variables have direct and clear impact on employee retention (i.e. whether they leave the company or continue to work)
2. Plot bar charts showing impact of employee salaries on retention
3. Plot bar charts showing corelation between department and employee retention
4. Now build logistic regression model using variables that were narrowed down in step 1
Measure the accuracy of the model

"""

"""df = pd.read_csv('HR_comma_sep.csv')
retain = df[df.left == 0]


pd.crosstab(df.salary, df.left).plot(kind='bar')
mpt.show()

pd.crosstab(df.Department, df.left).plot(kind='bar')
mpt.show()

dummies = pd.get_dummies(df['salary'])
ndf = pd.concat([df, dummies], axis='columns')

ndf = ndf.drop(['last_evaluation', 'time_spend_company', 'Work_accident', 'left', 'Department', 'salary'],
               axis='columns')

x_train, x_test, y_train, y_test = model_selection.train_test_split(
    ndf, df['left'], test_size=0.3)

logreg = linear_model.LogisticRegression()

logreg.fit(x_train, y_train)

res = logreg.predict(x_test)
"""