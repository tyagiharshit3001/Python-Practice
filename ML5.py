import pandas as pd
import matplotlib.pyplot as mpt
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import seaborn as sb
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

from sklearn.datasets import load_iris

"""
digits = load_digits()

#mpt.gray()
#mpt.matshow(digits.images[5])

x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2)

log2 = LogisticRegression(solver='lbfgs', max_iter=3000)

log2.fit(x_train, y_train)

res = log2.predict(x_test)

confusion = confusion_matrix(y_test, res)

sb.heatmap(confusion, annot=True)
mpt.title('Confusion Matrix')
mpt.xlabel('Predicted values')
mpt.ylabel('True Values')
mpt.show()
"""

"""
Exercise: Use sklearn.datasets iris flower dataset to train your model using logistic regression. You need to figure out accuracy of your model and use that to predict different samples in your test dataset. In iris dataset there are 150 samples containing following features,

1. Sepal Length
2. Sepal Width
3. Petal Length
4. Petal Width

Using above 4 features you will clasify a flower in one of the three categories,

1. Setosa
2. Versicolour
3. Virginica
"""

iris = load_iris()
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3)


log2 = LogisticRegression()

log2.fit(x_train, y_train)

res = log2.predict(x_test)

# Classifying flower type
flower = iris.target_names[log2.predict(x_test)]

confusion = confusion_matrix(y_test, res)
sb.heatmap(confusion, annot=True)
mpt.title('Confusion Matrix')
mpt.xlabel('Predicted values')
mpt.ylabel('True Values')
mpt.show()


