def fun(a):
    if a==0:
        return 200
    print(a)
    t=fun(a - 1)
    return t
x=int(input("enter the no:"))
print(fun(x))
