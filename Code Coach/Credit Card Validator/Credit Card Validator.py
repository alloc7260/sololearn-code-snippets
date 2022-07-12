'''
You need to verify if the given credit card number is valid. For that you need to use the Luhn test.

Here is the Luhn formula:
1. Reverse the number.
2. Multiple every second digit by 2. 
3. Subtract 9 from all numbers higher than 9.
4. Add all the digits together.
5. Modulo 10 of that sum should be equal to 0. 

Task: 
Given a credit card number, validate that it is valid using the Luhn test. Also, all valid cards must have exactly 16 digits.

Input Format:
A string containing the credit card number you need to verify.

Output Format:
A string: 'valid' in case the input is a valid credit card number (passes the Luhn test and is 16 digits long), or 'not valid', if it's not.

Sample Input:
4091131560563988

Sample Output:
valid

Explanation: Let's run the Luhn test for our input:
Reverse: 8893650651311904
Multiplying the even positions by 2: 8 16 9 6 6 10 0 12 5 2 3 2 1 18 0 8
Subtract 9 from >9: 8 7 9 6 6 1 0 3 5 2 3 2 1 9 0 8
The sum: 70
70 Modulo 10 is 0.
The input passed the Luhn test and contains 16 digits, making it a valid credit card number.
'''

card = input()
number_lst = list(map(int, (i for i in card))) #convert string to list of numbers
reverse_lst = number_lst[::-1] #step1
reverse_lst[1::2] = [x*2 for x in reverse_lst[1::2]] #step2
reverse_lst = [i-9 if i>9 else i for i in reverse_lst] #step3
if (len(card) == 16) and (sum(reverse_lst) % 10 == 0):print('valid') #step4&5
else:print('not valid')
