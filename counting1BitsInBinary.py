d  = 1000

b = bin(d).replace('0b','')
h = hex(int(b))

c = 0
for i in b:
    if i=='1':
        c+=1

print(c)

# list comprehension

print(sum(1 for x in b if x=='1'))