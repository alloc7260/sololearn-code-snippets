'''
You need to calculate exactly how many days have passed between two dates.

Task:  
Calculate how many days have passed between two input dates, and output the result. 

Input Format: 
Two strings that represent the dates, first date should be the older date. 
Date format: Month DD, YYYY

Output Format: 
A number representing the number of days between the two dates.

Sample Input: 
August 15, 1979
June 15, 2018

Sample Output: 
14184

Explanation: 
14184 days have passed between the two input days.
'''

from datetime import datetime,date
d = {"January":1,
      "February":2,
      "March":3, 
      "April":4,
      "May":5,
      "June":6,
      "July":7,
      "August":8,
      "September":9,
      "October":10,
      "November":11,
      "December":12}
date1 = input().split()
date2 = input().split()
print(str(date(int(date2[2]),d[date2[0]],int(date2[1][:-1]))-date(int(date1[2]),d[date1[0]],int(date1[1][:-1]))).split()[0])
