'''
Building a Logistic Regression model.

Task
You are given a feature matrix and a single datapoint to predict. Your job will be to build a Logistic Regression model with the feature matrix and make a prediction (1 or 0) of the single datapoint.

Input Format
First line: Number of data points in the feature matrix (n)
Next n lines: Values of the row in the feature matrix, separated by spaces
Next line: Target values separated by spaces
Final line: Values (separated by spaces) of a single datapoint without a target value

Output Format
Either 1 or 0

Sample Input
6
1 3
3 5
5 7
3 1
5 3
7 5
1 1 1 0 0 0
2 4

Sample Output
1

https://api.sololearn.com/DownloadFile?id=3888

Explanation
We can see the points plotted on the graph above and the line that separates the data. The point (2, 4) is noted on the graph and you can see it is on the positive side of the line, so the result is 1.
'''

n = int(input())
X = []
for i in range(n):
    X.append([float(x) for x in input().split()])
y = [int(x) for x in input().split()]
datapoint = [float(x) for x in input().split()]

import pandas as pd
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X, y)
print(model.predict([datapoint])[0])
