i = 1
sum = 0
n = int(input('Enter the number you want to check'))
while i<n:
    if n%i==0:
        sum+=i
    i+=1
if sum==n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")