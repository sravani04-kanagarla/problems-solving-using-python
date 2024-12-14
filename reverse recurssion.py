def fun(a):
    if a==0:
        return 0
    print(a)
    fun(a - 1)
x=int(input("enter the no:"))
fun(x)
