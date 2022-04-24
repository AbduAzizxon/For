n=int(input('n = '))
a0=2
for i in range(1,n+1):
    an=2+1/a0
    a0=an
    print(an)