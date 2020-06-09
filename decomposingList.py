l = [1,2,3,54,4,6,7,4]
x = ['a','ab','abc']
# with *
print(*l)

# with join method for strings

print(" ".join(x))

# with join method for integers

print(" ".join(str(x) for x in l))