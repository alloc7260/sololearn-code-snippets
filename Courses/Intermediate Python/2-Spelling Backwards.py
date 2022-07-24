'''
Given a string as input, use recursion to output each letter of the strings in reverse order, on a new line.

Sample Input
HELLO

Sample Output
O
L
L
E
H

Complete the recursive spell() function to produce the expected result.
'''

def spell(txt):

    #for i in txt[::-1] : print(i) #-----------------------------------------
    if len(txt) == 0:
        return
    spell(txt[1:])
    print(txt[0])

txt = input()
spell(txt)
#why the hell is recursion needed
