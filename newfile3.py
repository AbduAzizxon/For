a=int(input("a = "))
b=int(input("b = "))
if b>a+1:
    for i in range(a+1,b):
        print(i, end=' ')
else:print('something went wrong')