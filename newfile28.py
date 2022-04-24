n=int(input('n = '))
x=float(input('x = '))
s=1+x/2
juft=1
toq=1
daraja=x
sign=-1
for i in range(3,2*n+1,2):
    toq*=(i-2)
    juft*=(i-1)
    daraja*=x
    s+=(sign*toq*daraja)/((i+1)*juft)
    sign*=-1
print(s)