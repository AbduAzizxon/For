n=int(input('n = '))
x=float(input('x = '))
s=x
juft=1
toq=1
for i in range(3,2*n+1,2):
    toq*=(i-2)
    juft*=(i-1)
    s+=toq*(x**i)/((juft*i))
print(s)