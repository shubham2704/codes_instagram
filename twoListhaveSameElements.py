l = [4,3,4,4,4]

l1 = [3,4,4,4,4]

# best method
print(set(l)== set(l1))

# using for loop

l.sort()
l1.sort()
c = 0
for x,y in zip(l,l1):
    if x==y:
        c+=1
print(len(l)==c and len(l1)==c)





