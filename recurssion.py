def fun(a):
    if a==0:
        return 0
    fun(a - 1)
    print(a)
x=int(input("enter the no:"))
fun(x)
