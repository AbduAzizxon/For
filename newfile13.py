n=int(input('n = '))
s=0
for i in range(1,n,2):
    s+=(1+i/10)
for j in range(2,n,2):
    s-=(1+j/10)
print(s)