n=int(input('n = '))
a=int(input('a = '))
b=a
s=1-a
for i in range(n-1):
    b*=a*(-1**i)
    s+=(-1*b)
print(s)