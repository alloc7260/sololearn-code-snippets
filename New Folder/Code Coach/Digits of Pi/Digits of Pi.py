'''
The constant Pi is defined as the ratio of a circle's circumference to its diameter.
Pi is an irrational number, meaning that it's digits never end or repeat in any known way. 

Task:
Given an integer N as input, find and output the Nth decimal digit of Pi.

Input Format:
An integer: 0<N<1000

Output Format: 
An integer, representing the Nth decimal digit of Pi.

Sample Input:
12

Sample Output:
9

Explanation: 
The 12th decimal digit of Pi is 9: 3.141592653589793...
'''

n=int(input())
"""def make_pi():
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    for j in range(1000):
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
        else:
            q, r, t, k, m, x = q*k, (2*q+r)x, t*x, k+1, (q(7*k+2)+r*x)//(t*x), x+2


my_array = []

for i in make_pi():
    my_array.append(str(i))

my_array = my_array[:1] + ['.'] + my_array[1:]
big_string = "".join(my_array)
print(big_string[n+1])
"""
try:
    # import version included with old SymPy
    from sympy.mpmath import mp
except ImportError:
    # import newer version
    from mpmath import mp

mp.dps = 1010
print(str(mp.pi)[n+1])
