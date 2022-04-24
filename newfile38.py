n=int(input('n = '))
a1=1
a2=2
a3=3
for i in range(4,n+1):
    an=a3+a2-2*a1
    a1=a2
    a2=a3
    a3=an
    print(an)