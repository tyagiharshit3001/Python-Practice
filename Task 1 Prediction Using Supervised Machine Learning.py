{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "a4a42ec3",
   "metadata": {},
   "source": [
    "# Author: Madhav Chandok\n",
    "\n",
    "\n",
    "# Gratuade Rotational Internship Program (GRIP) @ The Sparks Foundation\n",
    "\n",
    "\n",
    "# Task 1: Prediction Using Supervised ML (Level - Beginner)\n",
    "\n",
    "In this regression task I tried to predict the percentage of marks that a student is expected to score based upon the number of hours they studied. This is a simple linear regression task as it involves just two variables.  \n",
    "\n",
    "We will use Python Scikit-Learn library for machine learning which is used to implement regression functions. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c5561a4c",
   "metadata": {},
   "source": [
    "## Importing Required Libraries for the Project"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "20827504",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Importing the required libraries\n",
    "\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9e7fbe48",
   "metadata": {},
   "source": [
    "## Step 1: Reading the Data from Source URL"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "63c9c920",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data has been imported from the location\n",
      "Import Successful\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Hours</th>\n",
       "      <th>Scores</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2.5</td>\n",
       "      <td>21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>5.1</td>\n",
       "      <td>47</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3.2</td>\n",
       "      <td>27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>8.5</td>\n",
       "      <td>75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>3.5</td>\n",
       "      <td>30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>1.5</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>9.2</td>\n",
       "      <td>88</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>5.5</td>\n",
       "      <td>60</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>8.3</td>\n",
       "      <td>81</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>2.7</td>\n",
       "      <td>25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>7.7</td>\n",
       "      <td>85</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    Hours  Scores\n",
       "0     2.5      21\n",
       "1     5.1      47\n",
       "2     3.2      27\n",
       "3     8.5      75\n",
       "4     3.5      30\n",
       "5     1.5      20\n",
       "6     9.2      88\n",
       "7     5.5      60\n",
       "8     8.3      81\n",
       "9     2.7      25\n",
       "10    7.7      85"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Reading data from remote link\n",
    "\n",
    "url = r\"http://bit.ly/w-data\"\n",
    "student_data = pd.read_csv(url)\n",
    "\n",
    "print(\"Data has been imported from the location\")\n",
    "print(\"Import Successful\")\n",
    "\n",
    "student_data.head(11)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5190bc54",
   "metadata": {},
   "source": [
    "## Step 2: Input Data Visualization (Graph Plotting: Hours v/s Percentage)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9627a17f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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S5cuZfXq1V2/uQ7069ePIUOG0Ldv33KHYmYVrmoT/9KlS9lyyy0ZNmwYksodTllFBMuXL2fp0qUMHz683OGYWYWr2q6e1atXM2DAgLpP+gCSGDBggL/9mFWoab+bRtNzTR/a1vRcE9N+N60s8VRt4gec9Av4b2FWucZsP4bjbzx+XfJveq6J4288njHbjylLPFXb1WNmVi0ahzcy87iZHH/j8UxumMz05unMPG4mjcMbyxJPVbf4y+2CCy5gr732YuTIkYwePZq5c+eWOyQzq1CNwxuZ3DCZH9z3AyY3TC5b0oc6Sfx59K/94Q9/4LbbbmPBggU88sgj3H333ey4445dH9iBtWvX9vhYM6t8Tc81Mb15OlMOmcL05unr5aRSqovEn0f/2rJlyxg4cCCbbJItiDRw4EC233575s2bxyc+8QlGjRrF2LFjWblyJatXr+bkk09mn332Yd9996WpKYvjqquu4uijj+bQQw9lwoQJvPXWW3zlK19h7Nix7Lvvvtxyyy0APP7444wdO5bRo0czcuRInnnmmQ38i5hZKbXmnJnHzeT8xvPXdfuULflHRMU/9t9//2jriSeeWG9bZ2Yvnh0Dpw2MKbOnxMBpA2P24tndOr6tlStXxqhRo2LEiBExefLkmDNnTrz77rsxfPjwePDBByMi4o033og1a9bERRddFCeffHJERCxatCh23HHHeOedd+LKK6+MHXbYIZYvXx4REd/5znfil7/8ZURErFixIkaMGBGrVq2Kf/7nf46rr746IiLefffdePvtt9uNqbt/EzMrjQsfuHC9nDN78ey48IELc70u0Bzt5NS6Gdwt7F+bcsiUDe5f22KLLZg/fz73338/TU1NTJw4ke9973sMHjyYMWOybxJbbbUVAA888ACnn346ALvvvjs77bQTTz/9NACHHXYY/fv3B+Cuu+7i1ltv5aKLLgKyKatLlixh3LhxXHDBBSxdupTPf/7zjBgxYoNiN7PSOuug9Vf4bBzeWLZ+/rpJ/G371xqHbfgfvU+fPowfP57x48ezzz77cMkll3T7HJtvvvm65xHBTTfdxG67fXht7j322IMDDjiA22+/nSOPPJJLL72UQw89dINiN7P6VRd9/Hn0rz311FMf6mtfuHAhe+yxB8uWLWPevHkArFy5krVr13LwwQdzzTXXAPD000+zZMmS9ZI7wOGH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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Plotting the graph of Distribution of Scores with respect to Hours of Study\n",
    "\n",
    "student_data.plot(x='Hours', y='Scores', style='gx')\n",
    "\n",
    "plt.title(\"Hours v/s Percentage\")\n",
    "plt.xlabel(\"Hours of Study\")\n",
    "plt.ylabel(\"Percentage Score\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f1f37238",
   "metadata": {},
   "source": [
    "From the graph we can clearly see that there is a positive linear relation between the number of hours of study and the percentage scored."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9004b375",
   "metadata": {},
   "source": [
    "## Step 3: Data Preprocessing\n",
    "\n",
    "This setp involved the distrbution of data into \"attributes\" (inputs) and \"labels\" (outputs)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "af6001b3",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = student_data.iloc[:, :1].values\n",
    "y = student_data.iloc[:, -1].values"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b4a48038",
   "metadata": {},
   "source": [
    "## Step 4: Model Training\n",
    "\n",
    "We are going to split this data into training and test sets. \n",
    "\n",
    "We'll do this by using Scikit-Learn's built-in train_test_split() method:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "8a340018",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Training Complete\n"
     ]
    }
   ],
   "source": [
    "#Importing train_test_split from SciKit-Learn's Library\n",
    "from sklearn.model_selection import train_test_split\n",
    "#Importing Linear Regression module from SciKit-Learn's Library\n",
    "from sklearn.linear_model import LinearRegression\n",
    "\n",
    "\n",
    "x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)\n",
    "\n",
    "regressor = LinearRegression()\n",
    "regressor.fit(x_train.reshape(-1,1), y_train)\n",
    "\n",
    "print(\"Training Complete\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "40025ede",
   "metadata": {},
   "source": [
    "## Step 5: Plotting the Line of Regression\n",
    "\n",
    "Now since our model is trained now, its the time to visualize th best-fit line of regression."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "b7fddd8a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Plotting the regression line\n",
    "regress_line = regressor.coef_ * x + regressor.intercept_\n",
    "\n",
    "#Plotting for the test data\n",
    "plt.scatter(x,y,marker='x', color='green')\n",
    "plt.plot(x,regress_line, color='red')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b2d7f415",
   "metadata": {},
   "source": [
    "## Step 6: Making Predictions\n",
    "\n",
    "Now that we have trained our algorithm, it's the time to test the model by making some predictions.\n",
    "\n",
    "For this we wil use our test data set."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "030ace62",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hours of Study: \n",
      "[[1.5]\n",
      " [3.2]\n",
      " [7.4]\n",
      " [2.5]\n",
      " [5.9]]\n",
      "\n",
      " Percentage respectively to their hours of study: \n",
      "[16.88414476 33.73226078 75.357018   26.79480124 60.49103328]\n"
     ]
    }
   ],
   "source": [
    "#Testing Data Set\n",
    "print(\"Hours of Study: \")\n",
    "print(x_test)\n",
    "\n",
    "#Making Prediction for Test Data Set\n",
    "y_prediction = regressor.predict(x_test)\n",
    "print(\"\\n Percentage respectively to their hours of study: \")\n",
    "print(y_prediction)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4e3ba8c2",
   "metadata": {},
   "source": [
    "## Step 7: Comparing Actual result to the Predicted Model Result\n",
    "\n",
    "In this section we will comparing the predicted data with the actual result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "fb809d32",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Actual</th>\n",
       "      <th>Predicted</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>20</td>\n",
       "      <td>16.884145</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>27</td>\n",
       "      <td>33.732261</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>69</td>\n",
       "      <td>75.357018</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>30</td>\n",
       "      <td>26.794801</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>62</td>\n",
       "      <td>60.491033</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Actual  Predicted\n",
       "0      20  16.884145\n",
       "1      27  33.732261\n",
       "2      69  75.357018\n",
       "3      30  26.794801\n",
       "4      62  60.491033"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Comparing Actual v/s Predicted\n",
    "\n",
    "data = pd.DataFrame({'Actual': y_test, 'Predicted': y_prediction})\n",
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "88c3e857",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Training Score:  0.9515510725211552\n",
      "Test Score:  0.9454906892105355\n"
     ]
    }
   ],
   "source": [
    "#Estimating training and test score\n",
    "\n",
    "print(\"Training Score: \", regressor.score(x_train, y_train))\n",
    "print(\"Test Score: \", regressor.score(x_test,y_test))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "68df91c1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 360x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Plotting the Bar to depict the difference between the actual and predicted value\n",
    "\n",
    "data.plot(kind='bar', figsize=(5,5), color=['dodgerblue','deeppink'])\n",
    "plt.grid(which='major', linewidth='0.5')\n",
    "plt.grid(which='minor', linewidth='0.5')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "3fdefdc4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "No of Hours: 5.47\n",
      "Predicted Percentage: 56.22945099054771\n"
     ]
    }
   ],
   "source": [
    "#Testing the model with our own data\n",
    "\n",
    "hours = 5.47\n",
    "test = np.array([hours])\n",
    "test = test.reshape(-1,1)\n",
    "own_prediction = regressor.predict(test)\n",
    "\n",
    "print(\"No of Hours: {}\".format(hours))\n",
    "print(\"Predicted Percentage: {}\".format(own_prediction[0]))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bf22abcc",
   "metadata": {},
   "source": [
    "## Step 8: Evaluation our Pediction Model\n",
    "\n",
    "The final step is to evaluate the performance of algorithm. This step is particularly important to compare how well different algorithms perform on a particular dataset. Here different errors have been calculated to compare the model performace and predict the accuracy."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "839a0907",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean Absolute Error:  4.183859899002975\n",
      "Mean Squared Error:  21.598769307217406\n",
      "Root Mean Squared Error:  4.647447612100367\n"
     ]
    }
   ],
   "source": [
    "from sklearn import metrics\n",
    "\n",
    "print(\"Mean Absolute Error: \", metrics.mean_absolute_error(y_test, y_prediction))\n",
    "print(\"Mean Squared Error: \",metrics.mean_squared_error(y_test,y_prediction))\n",
    "print(\"Root Mean Squared Error: \",np.sqrt(metrics.mean_squared_error(y_test,y_prediction)))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "047f3cc7",
   "metadata": {},
   "source": [
    "## Conclusion\n",
    "\n",
    "I have successfully able to carry-out Prediction using Supervised Machine Learning.\n",
    "I have also evaluate my model's performance on the basis of various parameters.\n",
    "\n",
    "# Thank You"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
