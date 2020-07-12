n = int(input("Enter the number of rows in floyd's triangle"))
a = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(a,end='')
        a+=1
    print()
