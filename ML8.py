import pandas as pd
import matplotlib.pyplot as mpt
from sklearn.datasets import load_digits
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
import seaborn as sb
from sklearn.preprocessing import LabelEncoder

"""
Random Forest Algorithm: RFA
    1. Divide dataset into sub datasets
    2. For each make decision tree
    3. Compile the outcome of each tree and return classification based on majority of votes.
"""

"""
digits = load_digits()

df = pd.DataFrame(digits.data, columns=digits.feature_names)
df['target'] = digits.target
df['img_digit'] = df.target.apply(lambda z: digits.target_names[z])

mpt.gray()
for i in range(5):
    mpt.matshow(digits.images[i])

x = df.drop(['target', 'img_digit'], axis='columns')
y = df.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=True)

rfc = RandomForestClassifier(n_estimators=2000)

rfc.fit(x_train, y_train)

res = rfc.predict(x_test)

confusion = confusion_matrix(y_test, res)
sb.heatmap(confusion, annot=True)
mpt.title('Confusion Matrix')
mpt.xlabel('Predicted values')
mpt.ylabel('True Values')
mpt.show()
"""

iris = load_iris()

df2 = pd.DataFrame(iris.data, columns=iris.feature_names)
df2['target'] = iris.target
df2['flower_names'] = df2.target.apply(lambda z: iris.target_names[z])

x = df2.drop(['target', 'flower_names'], axis='columns')
y = df2.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=True)

rfc2 = RandomForestClassifier()

rfc2.fit(x_train, y_train)

res2 = rfc2.predict(x_test)

res2 = pd.DataFrame(res2, columns=['Flowers_name'])

le = LabelEncoder()

for i in iris.feature_names:
    res2[i] = le.inverse_transform(res2[i])


"""confusion = confusion_matrix(y_test, res2)
sb.heatmap(confusion, annot=True)
mpt.title('Confusion Matrix')
mpt.xlabel('Predicted values')
mpt.ylabel('True Values')
mpt.show()"""
