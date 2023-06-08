from array import *

def decor(fun):
    def inner():
        a = fun()
        add = a+5
        return add

    return inner

def num():
    return 10

redsult_fun = decor(num)
print(redsult_fun())

@decor
def num():
    return 10

print(num())

def show(ar):
    print("Passed Array ar : ",ar)
    print(type(ar))
    for i in ar:
        print(i)
        return ar
    print("=============")
    a = array('i',[101,102,103,104])
    y = show(a)
    print("Return Array Y : ",y)
    print(type(y))
    for i in y :
        print(i)