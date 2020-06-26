"""
Description

A number is said to be sunny when 1 added to that number, the square root of it becomes a whole numbe.
For example:
3 is a sunny number, as:
(3+1)=4 and sqrt(4)=2 which is an integer

"""

import math

num = int(input('Enter the number'))
x = math.sqrt(num+1)
if int(x)==x:
    print(f'{num} is a sunny number')
else:
    print(f'{num} is not a sunny number')