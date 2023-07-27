import math
import joblib
import matplotlib.pyplot as mpt
import pandas as pd
import word2number
from word2number import w2n
from sklearn import linear_model
import pickle

# ML model for prediction using linear regression

"""
# Step 1: Exploring dataset
df = pd.read_excel('sample-xls-file-for-testing.xls', 'Sheet1')

# print(df.to_markdown())
mpt.xlabel('Gross Sales')
mpt.ylabel('Profit')
mpt.title('Sale-Profit graph')
mpt.scatter(df.Gross_Sales, df.Profit, color='orange', marker='+')


mpt.show()

# creating linear regression object
reg = linear_model.LinearRegression()

# fitting data
reg.fit(df[['Gross_Sales']], df.Profit)

mpt.plot(df.Gross_Sales, reg.predict(df[['Profit']]), color='blue')

mpt.show()
# predicting values
print(reg.predict([[18540]]))

#saving file model 
joblib.dump(reg, "model_jblb")
#mj = joblib.load("model_jblb")

"""
"""

#saving file model 
with open("model_pkkl","wb") as f:
    pickle.dump(reg, f)

with open("model_pkkl", "rb") as f:
    mp = pickle.load(f)

print(mp.predict([[18540]]))

"""

# moving ahead with ML
"""

#Getiing values used (Y= mx + c) m= coef, c=intercept
print(reg.coef_, reg.intercept_)
print(reg.predict([[18540]]))
print(reg.coef_ * 18540 + reg.intercept_)

#Getting predictions and writing them back to CSV file
df2 = pd.read_excel('Book2.xlsx', 'Sheet1')
p = reg.predict(df2)
df2['Predicted Profit'] = p
df2.to_csv('Mypredicted_profit.csv', index=False)

#plotting regression graph line
mpt.plot(df.Gross_Sales, reg.predict(df[['Gross_Sales']]))
"""
# Canada per capita income data exercise
"""
#exercise for predicting income in 2021
df3 = pd.read_csv('canada.csv')
print(df3.to_markdown())
mpt.xlabel('Years')
mpt.ylabel('Per Capita Income (in US$)')
mpt.title('Canadian Income graph')
mpt.scatter(df3.Year, df3.Per_capita_income, marker="+", color='green')
reg2 = linear_model.LinearRegression()
reg2.fit(df3[['Year']], df3.Per_capita_income)
print([[reg2.predict([[2021]])]])
"""

# TSF Score prediction
"""
# TSF score prediction based on study hours
df4 = pd.read_csv('Tsf Dataset.csv')
#df4.set_index('Hours', inplace=True)
print(df4.to_markdown())
mpt.xlabel('Study (hours/day)')
mpt.ylabel('Score')
mpt.title('Student Progress Graph')
mpt.scatter(df4.Hours, df4.Scores, marker="+", color='g')
reg = linear_model.LinearRegression()
reg.fit(df4[['Hours']], df4.Scores)
print("\n\nThe predicted score for the student who study for 9.25 hrs/day is ", float(reg.predict([[9.25]])))
mpt.show()
"""

# Multi-variable linear regression hiring exercise

df5 = pd.read_csv('hiring exercise.csv', index_col=False)
df5.experience.fillna('zero', inplace=True)
df5.experience = df5.experience.apply(word2number.w2n.word_to_num)
df5['test_score(out of 10)'] = df5['test_score(out of 10)'].fillna(math.floor(df5['test_score(out of 10)'].mean()))
reg3 = linear_model.LinearRegression()
reg3.fit(df5[['experience', 'test_score(out of 10)', 'interview_score(out of 10)']], df5['salary($)'])
print("The Salary of employee having 2 yr experience, test score as 9 and interview score as 6 is $",
      int(reg3.predict([[2, 9, 6]])))
mpt.plot(df5)
mpt.show()
"""
print("The Salary of employee having 12 yr experience, test score as 10 and interview score as 10 is $",
      int(reg3.predict([[12, 10, 10]])))
"""

"""
# Gradient Decent algo implementation for mean square error
def grad_dec(x, y):
    m_curr = b_curr = 0
    iterations = 10000
    n = len(x)
    cost_prev = 0
    learning_rate = 0.0002
    for i in range(iterations):
        y_pred = m_curr * x + b_curr
        cost = (1 / n) * sum([val ** 2 for val in (y - y_pred)])
        md = -(2 / n) * sum(x * (y - y_pred))
        bd = -(2 / n) * sum(y - y_pred)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        if math.isclose(cost, cost_prev, rel_tol=1e-20):
            break
        cost_prev = cost
        print("m {}, b {} , cost {}, iterations {} ".format(m_curr, b_curr, cost, i))
        mpt.plot()


df = pd.read_csv("grad_dec.csv")
x = df["math"]
y = df["cs"]

grad_dec(x, y)

mpt.show()
"""
