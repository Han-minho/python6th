#Example 1
def add(x,y):
    z = x + y
    print("Addition1 : ",z)

add(5,2)

#Example 2
def add(*num):
    z = num[0]+num[1]+num[2]
    print("Addition2 : ",z)

add(5,2,4)

#Example3
def add(x,*num):
    z = x+num[0]+num[1]
    print("Addition3 : ", z)
add(5,2,4)

#가변 키워드 인자 사용법
def add(x,**num):
    z = x + num["a"]+num["b"]+num["c"]
    print("Addition4 : ",z)

add(3,a=5,b=2,c=4,d=5)


def show():
    x = 10
    print(x)

show()

def add(y):
    x = 10
    print(x)
    print(x+y)

add(20)

a = 50
def show():
    x = 10
    print(x) # local
    print(a) # global

show()
print("Gobal Variable a : ",a)

#전역변수 사용법
# i = 0
# def myfun():
#     a = i+1
#     print("My Function : ",a)
#
# myfun()
# print("Gobal Variable a : ",a)


# global인지 local인지 확실지 않아 에러

#  def myfun(i):
#      b = i + 1
#     print("My Function b : ",b)
#
#
# myfun()

a = 50
def show():
    a = 10
    print("show~A : ",a)

show()
print("A : ",a)

def show2():
    global a
    print("show2~A : ",a)
    a=20
    print("show2~A2 : ",a)

show2()
print("A : ",2)
