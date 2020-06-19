def fact(n):
    f = 1
    i = 1
    while i<=n:
        f = f*i
        i+=1
    return f

#Lines represents how many 
#lines of triangel we need
lines = 6

for x in range(lines):
    for y in range(x+1):
        print(fact(x)//(fact(y)*fact(x-y)), " ",end='')
    print()