import sys

#재귀함수 호출
print("default : ",sys.getrecursionlimit())
sys.setrecursionlimit(3000)
print("setting:",sys.getrecursionlimit())


#재귀함수
i = 0
def myfun():
    global i
    i += 1
    print("My Function : ",i)
    myfun()

myfun()