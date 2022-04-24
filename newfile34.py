n=int(input('n = '))
a1=1
a2=2
for i in range(2,n+1):
    an=(a1+2*a2)/3
    a1=a2
    a2=an
    print(an)