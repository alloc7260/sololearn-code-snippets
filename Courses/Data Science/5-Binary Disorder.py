'''
Confusion matrix of binary classification.

For binary classifications, a confusion matrix is a two-by-two matrix to visualize the performance of an algorithm. Each row of the matrix represents the instances in a predicted class while each column represents the instances in an actual class.

Task
Given two lists of 1s and 0s (1 represents the true label, and 0 represents the false false) of the same length, output a 2darrary of counts, each cell is defined as follows

Top left: Predicted true and actually true (True positive)
Top right: Predicted true but actually false (False positive)
Bottom left: Predicted false but actually true (False negative)
Bottom right: Predicted false and actually false (True negative)

Input Format
First line: a list of 1s and 0s, separated by space. They are the actual binary labels.
Second line: a list of 1s and 0s, the length is the same as the first line. They represented the predicted labels.

Output Format
A numpy 2darray of two rows and two columns, the first row contains counts of true positives and false positives and the second row contains counts of false negatives and true negatives.

Sample Input
1 1 0 0
1 0 0 0

Sample Output
[[1., 0.],
[1., 2.]]

Explanation
Among the actual labels, there are 2 trues and 2 falses. One true label was correctly predicted as true and the other was incorrectly predicted as false; that is, one true positive and one false negative. Of the two false labels, both were correctly predicted; that is, zero false positive and two true negatives.
'''

y_true = [int(x) for x in input().split()]
y_pred = [int(x) for x in input().split()]

from sklearn.metrics import confusion_matrix

print((confusion_matrix(y_pred,y_true, labels=[1,0]))/1)

#labels used for swaping 1s and 0s with eachother
#/1 is used for converting integer to float
