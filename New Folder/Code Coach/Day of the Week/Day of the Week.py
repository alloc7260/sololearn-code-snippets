'''
You receive a date and need to know what day of the week it is. 
 
Task: 
Create a program that takes in a string containing a date, and outputs the day of the week.

Input Format: 
A string containing a date in either "MM/DD/YYYY" format or "Month Day, Year" format.

Output Format: 
A string containing the day of the week from the provided date.

Sample Input: 
11/19/2019

Sample Output: 
Tuesday

Explanation: 
19 November 2019 is a Tuesday.
'''

from datetime import datetime
ip = input()
date = ip.split("/")
if len(date)==3 :
 date = list(map(int,date))
 print(datetime(date[2],date[0],date[1]).strftime("%A"))
else :
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
      "December":12
     }
 date = ip.split()
 print(datetime(int(date[2]),d[date[0]],int(date[1][:-1])).strftime("%A"))

"""
# Day of the Week - Code Coach

import datetime as dt

inp = input()

if not inp[0].isalpha():

    d = [int(p) for p in inp.split('/')]     
    dy = dt.datetime(d[2], d[0], d[1])
    print(dy.strftime("%A"))

else:

    d = [p for p in inp.split(',')]
    dd = [p for p in d[0].split('
     ')]
    m = dt.datetime.strptime(dd[0], '%B').month
    dy = dt.datetime(int(d[1]), m, int(dd[1]))
    print(dy.strftime("%A"))

'''
Sample Input: 
11/19/2019

Sample Output: 
Tuesday
----------------
Test Case #1
Sample Input: 
11/20/2019

Sample Output: 
Wednesday
----------------
Test Case #2
Sample Input: 
July 20, 2020
{}
Sample Output: 
Monday
'''

# Keep learning & happy coding :D

'''
now = dt.datetime.now()
print(now.strftime("%A"))
wdy = dt.datetime.today().weekday()
https://www.journaldev.com/23365/python-string-to-datetime-strptime
https://strftime.org
'''
"""
