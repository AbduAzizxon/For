n=int(input('n = '))
a0=1
for K in range(1,n+1):
    an=(a0+1)/K
    a0=an
    print(an)