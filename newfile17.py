n=4
a=4
b=a
s=1+a

for i in range(1,n,1):
    b*=a
    s+=b
print(s)