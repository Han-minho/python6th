import sys
from array import *


def val(list):
    print("Inside Function Before Append : ",list,id(list))
    list.append(4)
    print("Inside Function After Append : ", list, id(list))

list = [1,2,3]
print("Before Calling Function : ",list,id(list))
val(list)
print("After Calling function : ",list,id(list))

def val(x):
    print("Inside : ",x,",",id(x))
    x += 1
    print("Inside After : ",x,",",id(x))

print("=====================================")
x = 10
print("Before Calling : ",x,",",id(x))
val(x)
print("After Calling : ",x,",",id(x))