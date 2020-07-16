def hcf(a,b):
    if a==b:
        return a
    else:
        return hcf(b,a%b)

a = int(input('Enter First Number : '))
b = int(input('Enter Second Number : '))
ans = hcf(a,b)
print(f'HCF of Numbers {a} and {b} is : {ans}')