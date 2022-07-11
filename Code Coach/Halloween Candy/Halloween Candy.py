'''
You go trick or treating with a friend and all but three of the houses that you visit are giving out candy. One house that you visit is giving out toothbrushes and two houses are giving out dollar bills. 

Task
Given the input of the total number of houses that you visited, what is the percentage chance that one random item pulled from your bag is a dollar bill? 

Input Format 
An integer (>=3) representing the total number of houses that you visited. 

Output Format
A percentage value rounded up to the nearest whole number.

Sample Input
4

Sample Output 
50

Explanation 
If you visited four houses, one would be candy, two would be dollars, and one would be a toothbrush. A 2 in 4 chance is 50%.
'''

houses = int(input())
#probability of dollar per one house
probability_dollar=2/houses
#percentage of dollar for all houses
percentage_dollar=probability_dollar*100
#rounding up value
import math
print(math.ceil(percentage_dollar))
