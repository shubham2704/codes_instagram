"""
Description 

A neon number is a number where the sum of digits of square of the number is equal to the number. The task is to check and print neon numbers in a range. Examples: Input : 9 Output : Neon Number Explanation: square is 9*9 = 81 and sum of the digits of the square is 9

"""

num = int(input('Enter the number : '))

sq = num*num
sum = 0

while sq>0:
    sum = sum + sq%10
    sq = sq//10

if sum == num:
    print(f'{num} is Neon Number.')
else:
    print(f'{num} is Not Neon Number.')