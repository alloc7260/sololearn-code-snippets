'''
In a matrix, or 2-d array X, the averages (or means) of the elements of rows is called row means.

Task
Given a 2D array, return the rowmeans.

Input Format
First line: two integers separated by spaces, the first indicates the rows of matrix X (n) and the second indicates the columns of X (p)
Next n lines: values of the row in X

Output Format
An numpy 1d array of values rounded to the second decimal.

2 2
1.5 1
2 2.9

Sample Output
[1.25 2.45]

Explanation
The first row has two numbers 1.5 and 1, thus the sum is 1.5 + 1 = 2.5 and the mean is then 2.5/2 = 1.25. Then for the second row, the average is calculated as (2 + 2.9)/2 = 4.9/2 = 2.45.
'''

'''
for simplicity i let 
r as rows (actually n) &
c as columns (actually p)
'''
#input number of rows & columns
r, c = [int(x) for x in input().split()]
#input matrix in array according r&c
ia=[]
for i in range(r):
    ia.append([float(j) for j in input().split()])

import numpy as np
#convert to numpy array
na=np.array(ia)
#print of mean
#axis = 1 for rows (horizontally)
#rounded by 2 decimal points
print(na.mean(axis=1).round(2))
