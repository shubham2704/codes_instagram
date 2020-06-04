n = 10

l = []
for i in range(1,n+1):
    l.append(i*i)
print(l)
# OR
print(*l)

# List compherihension

print(" ".join(str(x*x) for x in range(1,n+1)))
