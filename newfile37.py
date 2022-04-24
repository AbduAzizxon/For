n=int(input('n = '))
s=0
for i in range(1,n+1):
    d=i**i
    for j in range(1):
        s+=d
print(s)