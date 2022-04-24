x=abs(0.5)
n=3
s=0
for i in range(1,n+1):
    s+=(x**i)/(i*((-1)**(i-1)))
print(s)