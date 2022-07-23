'''
You want to convert the time from a 12 hour clock to a 24 hour clock. If you are given the time on a 12 hour clock, you should output the time as it would appear on a 24 hour clock.  

Task:  
Determine if the time you are given is AM or PM, then convert that value to the way that it would appear on a 24 hour clock.

Input Format: 
A string that includes the time, then a space and the indicator for AM or PM.

Output Format: 
A string that includes the time in a 24 hour format (XX:XX)

Sample Input: 
1:15 PM

Sample Output: 
13:15

Explanation:
1:00 PM on a 12 hour clock is equivalent to 13:00 on a 24 hour clock.
'''

ip1=list(input().split(" "))
ip2=list(ip1[0].split(":"))
(print(f"00:{ip2[1]}") if int(ip2[0])==12 else print(ip1[0].zfill(5))) if ip1[1]=="AM" else (print(ip1[0]) if int(ip2[0])==12 else print(f"{int(ip2[0])+12}:{ip2[1]}"))
