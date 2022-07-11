'''
You write a phrase and include a lot of number characters (0-9), but you decide that for numbers 10 and under you would rather write the word out instead. Can you go in and edit your phrase to write out the name of each number instead of using the numeral? 

Task: 
Take a phrase and replace any instances of an integer from 0-10 and replace it with the English word that corresponds to that integer.

Input Format: 
A string of the phrase in its original form (lowercase).

Output Format: 
A string of the updated phrase that has changed the numerals to words.

Sample Input: 
i need 2 pumpkins and 3 apples

Sample Output: 
i need two pumpkins and three apples

Explanation: 
You would update the phrase to change '2' to 'two' and '3' to 'three'.
'''

def f(str,s1,s2) :
	str=str.replace(s1,s2)
	return(str)
s=input()
ls=list(range(11))
lr=ls[::-1]
la=["ten","nine","eight","seven","six","five","four","three","two","one","zero"]
for i in ls :
	s=f(s,str(lr[i]),str(la[i]))
print(s)

# s=input()
# s=s.replace("10", "ten") 
# s=s.replace("0", "zero")
# s=s.replace("1", "one")
# s=s.replace("2", "two")
# s=s.replace("3", "three")
# s=s.replace("4", "four")
# s=s.replace("5", "five")
# s=s.replace("6", "six") 
# s=s.replace("7", "seven")
# s=s.replace("8", "eight")
# s=s.replace("9", "nine")
# print(s)
