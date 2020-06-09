n = 10
s = 0
for x in range(1,n+1):
    s+=x*x
print(s)


print(sum(x*x for x in range(1,n+1))) 