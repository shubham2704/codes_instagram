l = [1,2,3,'d',5,'free','live',8]

# VERSION-1

l1 = []
for i in l:
    if isinstance(i,int):
        l1.append(i)
print(l1)         

# VERSION-2

print([x for x in l if isinstance(x,int)])