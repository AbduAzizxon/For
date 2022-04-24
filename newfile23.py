n=int(input('n = '))
x=int(input('x = '))
f=1
s=x
sign=-1
for i in range(3,2*n+1,2):
    f*=i*(i-1)
    s+=sign*x**i/f
    sign*=-1
print(s)