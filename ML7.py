import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.datasets import load_digits

"""
Support Vector Machine: Support vector machine or SVM is a supervised machine learning algorithm used for both 
                        classification and regression. Its objective is to plot a hyperplane in n-D space that
                        distinctly classifies data points.
                        * Dimensions depends on features in dataset.
                        * For 1D a it will be a point.
                        * For 2D it will be a line.
                        * For 3D it will be a plane.
                        * For <3D Difficult to imagine but theoretically and mathematically it is possible.

Gamma: It means influence. (High--->close, Low----->far) in relation to hyperplane and distinct data points.
       * If gamma<< the model is too constrained and cannot handle the complexity of data.

Kernel Function: It takes data as input and transform it into required form of processing data.
                * Kernel is because of set of mathematical functions in SVM to provide a window for manipulating data.
                * Major Kernel Functions:
                    1. Gaussian Kernel: Used when there is no prior knowledge about data.
                    2. Gaussian Radial Base Function ('rbf'): Same as above with improved transformation.
                    3. Sigmoid Kernel ('sigmoid'): Used as activation function for neurons in ANN.
                                        Equivalent to two-layer perceptron model of neural network.
                    4. Polynomial Kernel ('poly'): Represents the similarity of vector in training set of data in 
                                                    feature space  over polynomial variables in original kernel.
                    5. Linear Kernel ('linear'): Used when data is linearly separable.
                    
Regularization: It is a technique that prevents over-fitting by reducing coefficients towards zero by adding extra 
                information to it.
                It allows to maintain all variables or features in model by reducing the magnitude of variables.
                It enhance accuracy and generalization of model.
                * In regularization technique, we reduce the magnitude of variable or feature by keeping the number
                  of features same.
    1. LASSO Regularisation:(Least Absolute Shrinkage and Selection Operation) Adds up absolute value of magnitude of 
                            coefficient as penalty of loss in function.
    2. Rigid Regularisation: Squares the magnitude of coefficient as penalty of loss in function.
    3. Drop-Out Regularisation: Random dropout of nodes in ANN during training.
"""






"""
iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
df['flower_names'] = df.target.apply(lambda x: iris.target_names[x])
satosa = df[df.target == 0]
versi = df[df.target == 1]
virg = df[df.target == 2]

plt.title('Iris Flower Data of Sepal')
plt.xlabel('Sepal length (cm)')
plt.ylabel('Sepal width (cm)')
plt.scatter(x=satosa['sepal length (cm)'], y=satosa['sepal width (cm)'], marker='*', color='green', label='Satosa')
plt.scatter(x=versi['sepal length (cm)'], y=versi['sepal width (cm)'], marker='+', color='red', label='Versicolor')
plt.scatter(x=virg['sepal length (cm)'], y=virg['sepal width (cm)'], marker='.', color='blue', label='Virginica')
plt.legend(loc="best", shadow=True, fontsize='small')
plt.show()

plt.title('Iris Flower Data of Petal')
plt.xlabel('Petal length (cm)')
plt.ylabel('Petal width (cm)')
plt.scatter(x=satosa['petal length (cm)'], y=satosa['petal width (cm)'], marker='*', color='green', label='Satosa')
plt.scatter(x=versi['petal length (cm)'], y=versi['petal width (cm)'], marker='+', color='red', label='Versicolor')
plt.scatter(x=virg['petal length (cm)'], y=virg['petal width (cm)'], marker='.', color='blue', label='Virginica')
plt.legend(loc="best", shadow=True, fontsize='small')
plt.show()

x = df.drop(['target', 'flower_names'], axis='columns')
y = df.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

svm = SVC()
svm.fit(x_train, y_train)
res = svm.predict(x_test)
score = svm.score(x_test, y_test)

confusion = confusion_matrix(y_test, res)
sb.heatmap(confusion, annot=True)
plt.title('Confusion Matrix')
plt.xlabel('Predicted values')
plt.ylabel('True Values')
plt.show()

"""

"""
Exercise:
Train SVM classifier using sklearn digits dataset (i.e. from sklearn.datasets import load_digits) and then,

1. Measure accuracy of your model using different kernels such as rbf and linear.
2. Tune your model further using regularization and gamma parameters and try to come up with highest accuracy score
3. Use 80% of samples as training data size

"""

digits = load_digits()

df2 = pd.DataFrame(digits.data, columns=digits.feature_names)
df2['target'] = digits.target
df2['img_digit'] = df2.target.apply(lambda z: digits.target_names[z])

x = df2.drop(['target', 'img_digit'], axis='columns')
y = df2.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=True)

# svm2 = SVC(kernel='linear')
svm2 = SVC(kernel='rbf')        # Greater then (kernel='linear')

svm2.fit(x_train, y_train)
res2 = svm2.predict(x_test)
score2 = svm2.score(x_test, y_test)

confusion = confusion_matrix(y_test, res2)
sb.heatmap(confusion, annot=True)
plt.title('Confusion Matrix')
plt.xlabel('Predicted values')
plt.ylabel('True Values')
plt.show()
