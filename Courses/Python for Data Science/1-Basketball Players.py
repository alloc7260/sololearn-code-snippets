'''
The given code includes a list of heights for various basketball players.
You need to calculate and output how many players are in the range of one standard deviation from the mean.

Output the result using the print statement.
'''

import numpy as np
players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
a=np.array(players)
b=np.mean(a)
c=np.std(a)
range = [b-c,b+c]
count=len(players)
for i in players :
    if i<range[0]:count-=1
    if i>range[1]:count-=1
print(count)
