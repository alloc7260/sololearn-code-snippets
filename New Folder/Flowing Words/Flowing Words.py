'''
If a sentence flows, the first letter of each word will be the same to the last letter of the previous word. 

Task:
Write a program that takes in a string that contains a sentence, checks if the first letter of each word is the same as the last letter of the previous word. If the condition is met, output true, if not, output false. 
Casing does not matter.

Input Format: 
A string containing a sentence of words.

Output Format: 
A string: true or false.

Sample Input:
this string gets stuck

Sample Output: 
true

Explanation: 
Each word begins with the letter that the previous word ends with, therefore the output is true.
'''

def func(sen):
    for i in range(len(sen)-1):
        if sen[i][-1] == sen[i+1][0]:
            if i==len(sen)-2:
                return "true"
        else:return "false"
print(func(input().split(" ")))
