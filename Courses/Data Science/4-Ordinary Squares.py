'''
Ordinary least squares for linear regression.

Ordinary least squares (OLS) is a method to estimate the parameters β in a simple linear regression, Xβ = y, where X is the feature matrix and y is the dependent variable (or target), by minimizing the sum of the squares of the differences between the observed dependent variable in the given dataset and those predicted by the linear function. Mathematically, the solution is given by the formula in the image, where the superscript T means the transpose of a matrix, and the superscript -1 means it is an inverse of a matrix.

Task
Given a 2D array feature matrix X and a vector y, return the coefficient vector; see the formula above.

Input Format
First line: two integers separated by spaces, the first indicates the rows of the feature matrix X (n) and the second indicates the columns of X (p)
Next n lines: values of the row in the feature matrix
Last line: p values of target y

Output Format
An numpy 1d array of values rounded to the second decimal.

Sample Input
2 2
1 0
0 2
2 3

Sample Output
[2. , 1.5]

Explanation
The feature matrix X has n = 2 rows and p = 2 features. Following the OLS solution, substitute X by np.array([[1. 0.], [0. 2.]] and y by np.array([2. 3.]), respectively, performing the matrix multiplication using tools in numpy results in np.array([2. 1.5]).
'''

n, p = [int(x) for x in input().split()]
X = []
for i in range(n):
    X.append([float(x) for x in input().split()])

y = [float(x) for x in input().split()]

import numpy as np

X_arr = np.array(X)
y_arr = np.array(y)
X_Tarr = X_arr.T #Transpose of X

beta=(np.linalg.inv(X_Tarr @ X_arr)) @ X_Tarr @ y_arr

#According to OLS formula

print (beta.round(2))
