import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as mpt
import seaborn as sb


"""
Decision Tree: It is an algorithm used for classification as well as for regression. But it is most suitable for 
                classification type of problems. It somewhere uses the concept of tree data structure in which 
                intermediate nodes are the features of dataset, branches defines the decision rules and 
                leaf nodes are describes the outcomes.
"""

"""
df = pd.read_csv('Sales_Details.csv')
df.head()

inp = df.drop('Profit', axis='columns')
tar = df.Profit

segment_le = LabelEncoder()
country_le = LabelEncoder()
product_le = LabelEncoder()

inp['country_n'] = segment_le.fit_transform(df['Country'])
inp['segment_n'] = country_le.fit_transform(df['Segment'])
inp['product_n'] = product_le.fit_transform(df['Product'])

inp.drop(
    ['Unnamed: 0', 'Country', 'Segment', 'Product', 'Discount_Band', 'Units_Sold', 'Manufacturing_Price', 'Sale_Price',
     'Gross_Sales', 'Discounts', 'Sales', 'COGS', 'Date', 'Month_Number', 'Month_Name', 'Year'], axis='columns',
    inplace=True)

d_tree_model = tree.DecisionTreeClassifier()
x_train, x_test, y_train, y_test = train_test_split(inp, tar, test_size=0.3)
d_tree_model.fit(x_train, y_train)

res = d_tree_model.predict(x_test)

confusion = confusion_matrix(y_test, res)
sb.heatmap(confusion, annot=True)
mpt.title('Confusion Matrix')
mpt.xlabel('Predicted values')
mpt.ylabel('True Values')
mpt.show()
"""

df2 = pd.read_csv('titanic.csv')

df2['Age'].interpolate(inplace=True)

df2.drop(['PassengerId', 'Name', 'SibSp', 'Parch', 'Ticket', 'Cabin', 'Embarked'], axis='columns', inplace=True)

inp2 = df2.drop(['Survived'], axis='columns')
tar2 = df2['Survived']

sex_le = LabelEncoder()

inp2['Sex_n'] = sex_le.fit_transform(inp2['Sex'])

inp2.drop(['Sex'], axis='columns', inplace=True)

d_tree_model2 = tree.DecisionTreeClassifier()
x_train, x_test, y_train, y_test = train_test_split(inp2, tar2, test_size=0.3)
d_tree_model2.fit(x_train, y_train)

res = d_tree_model2.predict(x_test)

