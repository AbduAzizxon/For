n=int(input('n = '))
s=1
for i in range(11,(n+1)*10):
    s*=i/10
print(s)