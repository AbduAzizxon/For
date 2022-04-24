n=int(input('n = '))
b=1
s=1
for i in range(1,n+1):
    b*=i**-1
    s+=b
print(s)