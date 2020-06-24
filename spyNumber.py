"""
Descsription

Spy Number. A number is a Spy number, if sum and product of all digits are equal. Example: Number 123 is a Spy number, 
sum of its digits is 6 (1+2+3 =6) and product of its digits is 6 (1x2x3 = 6), sum and product are same, thus, 123 is a spy number.

"""
sum = 0
prod = 0

n = int(input('Enter the number'))

while n>0:
    r = n%10
    sum = sum+r
    prod = prod*r
    n = n//10
if sum==prod:
    print(f'{n} is a Spy number')
else:
    print(f'{n} is not a Spy number')