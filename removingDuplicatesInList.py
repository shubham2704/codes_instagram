n = [1,3,4,5,3,6]

# Naive method
l = []
for i in n:
    if n.count(i)==1:
        l.append(i)
print(l)

# List comprehension

print([x for x in n if n.count(x)==1])