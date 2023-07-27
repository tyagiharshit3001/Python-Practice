import pandas as pd
import matplotlib.pyplot as mpt
from sklearn.datasets import load_digits
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
import seaborn as sb
from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

"""
Cross Validation: It is a cross validation procedure that can be used to evaluate the efficiency of the model 
                        towards the given data set. There can be three ways of evaluating model performance:
                        1. Training and testing on same dataset.
                        2. Splitting data into two sets (using train_test_split):
                            a) Training set
                            b) Test set
                        3. Using KFold: Divides the data into folds then out of them using one fold as test set and 
                        rest folds as training sets then evaluate model score for each case and different models.
                        4. Using Stratified KFold:

"""

"""
digits = load_digits()
df = pd.DataFrame(digits.data, columns=digits.feature_names)
df['target'] = digits.target
df['img_digit'] = df.target.apply(lambda z: digits.target_names[z])

x = df.drop(['target', 'img_digit'], axis='columns')
y = df.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=True)

lr = cross_val_score(LogisticRegression(max_iter=5000), digits.data, digits.target)
svm = cross_val_score(SVC(), digits.data, digits.target)
rfc = cross_val_score(RandomForestClassifier(n_estimators=30), digits.data, digits.target)
"""


"""
def get_score(model, X_train, X_test, Y_train, Y_test):
    model.fit(X_train, Y_train)
    return model.score(X_test, Y_test)


kf = KFold(n_splits=3)
stratKfold = StratifiedKFold(n_splits=3)

score_lr = []
score_svm = []
score_rForest = []

for train_index, test_index in kf.split(digits.data):
    x_train, x_test, y_train, y_test = digits.data[train_index], digits.data[test_index], digits.target[train_index], \
                                       digits.data[test_index]
    score_lr.append(get_score(LogisticRegression(max_iter=5000), x_train, x_test, y_train, y_test))
    score_svm.append(get_score(SVC(), x_train, x_test, y_train, y_test))
    score_rForest.append(get_score(RandomForestClassifier(), x_train, x_test, y_train, y_test))


print("Score for Logistic Regression", score_lr)
print("Score for SVM", score_svm)
print("Score for Random Forest", score_rForest)
"""

"""
Exercise: Which model is best for iris flower classification.
"""

iris = load_iris()

lr = cross_val_score(LogisticRegression(max_iter=1000), iris.data, iris.target)
svm = cross_val_score(SVC(), iris.data, iris.target)
rfc = cross_val_score(RandomForestClassifier(n_estimators=15), iris.data, iris.target)
dtc = cross_val_score(DecisionTreeClassifier(), iris.data, iris.target)
