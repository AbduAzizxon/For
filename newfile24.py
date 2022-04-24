n=int(input('n = '))
x=int(input('x = '))
f=1
sign=-1
s=1
for i in range(2,2*n,2):
    f*=i*(i-1)
    s+=sign*x**i/f
    sign*=-1
print(s)

from math import cos
print(cos(x))