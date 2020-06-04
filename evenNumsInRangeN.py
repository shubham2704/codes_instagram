n = 100
l = []
for i in range(2,n+1):
    if i%2==0:
        l.append(i)
print(l)

# List comprehension

print([x for x in range(2,n+1) if x%2==0])

# reducing 1 computattion

print([x for x in range(2,n+1,2)])