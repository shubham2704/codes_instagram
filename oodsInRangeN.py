n = 100

l = []
for i in range(1,n+1):
    if i%2!=0:
        l.append(i)
print(l)

# List comprehension
print([x for x in range(1,n+1) if x%2!=0])

# saving one computation
print([x for x in range(1,n+1,2)])