'''
A coyote is chasing a roadrunner and they start out 50 feet apart. If you know how fast they are both traveling, and how far the roadrunner is from safety, determine whether or not the coyote is able to catch the roadrunner. 
Both animals and the roadrunner's safe place are on a straight line.

Task: 
Determine whether or not the roadrunner made it to safety.

Input Format: 
Three integer values, the first value represents the distance the roadrunner is from safety, then the roadrunner's speed (feet/second) and then the coyote's speed (feet/second).

Output Format: 
A string that says 'Meep Meep' if the roadrunner made it, or 'Yum' if the coyote caught up to the roadrunner.

Sample Input: 
10 
5 
20

Sample Output: 
Meep Meep

Explanation: 
The roadrunner is safe because it took them 2 seconds to get to safety while the coyote only got 30 feet closer to the roadrunner in that same amount of time.
'''

rsafedistance = int(input())
rspeed = int(input())
cspeed = int(input())

# diatance traveled by c untill r reach at safezone
ctraveldistance = (rsafedistance/rspeed)*cspeed
# distance to travel by c to reach safezone
creachdistance = 50+rsafedistance

if ctraveldistance < creachdistance :
  print("Meep Meep")
else:
  print("Yum")
"""
d = int(input())
print ("Meep Meep" if d/int(input()) < (d+50)/int(input()) else "Yum")
"""
"""
rsafedistance = int(input())
csafedistance = 50 + rsafedistance

rspeed = int(input())
cspeed = int(input())

rsafetime = rsafedistance/rspeed
creachtime = csafedistance/cspeed

if rsafetime < creachtime :
  print("Meep Meep")
else:
  print("Yum")
"""
