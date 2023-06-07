print("인자를 받지 않는 함수")

def disp():
    name = "멋쟁이사자"
    print("Welcome to",name)

# 항수 실핼부
print("함수 실행")
disp()
disp()
disp()

def add():
    x = 10
    y = 20
    c = x + y
    print(c)

add()

print("인자를 정해지는 함수")
def add(y):
    x = 10.2334
    print(x + y)
    print(f"Formatted Output{x + y :6.2f}")

add(20)