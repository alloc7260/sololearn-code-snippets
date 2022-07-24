'''
Given a text as input, find and output the longest word.

Sample Input
this is an awesome text

Sample Output
awesome

Recall the split(' ') method, which returns a list of words of the string.
'''

txt = input()
arr=txt.split(" ")
longest_word=""
for word in arr :
 if len(word) > len(longest_word) :
  longest_word=word
print(longest_word)
