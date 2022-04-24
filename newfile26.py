n=int(input('n = '))
x=float(input('x = '))
s=x
sign=-1
for i in range(3,2*n+1,2):
    s+=sign*x**i/i
    sign*=-1
print(s)
    