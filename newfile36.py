n=int(input('n = '))
k=int(input('k = '))
s=0
for i in range(1,n+1):
    d=i**k
    for j in range(1):
        s+=d
print(s)