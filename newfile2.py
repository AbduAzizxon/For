a=int(input("a = "))
b=int(input("b = "))
if b>a:
    for i in range(a,b+1):
        print(i, end=' ')
else:print('something went wrong')