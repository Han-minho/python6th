import time


def make_dolcelatte():
    print("1. 얼음을 넣는다.")
    print("2. 연유를 30ml 넣는다.")
    print("3. 찬 우유를 넣는다.")
    print("4. 에소프레소샷을 넣는다.")

def make_blueberry_smoothie():
    print("1. 블루베리 20g을 넣는다.")
    print("2. 우유 300ml를 넣는다.")
    print("3. 얼음을 넣는다.")
    print("4. 믹서기에 간다.")

def make_simple_latte():
    print("1. 커피를 넣는다.")
    print("2. 우유를 넣는다.")
    print("3. 신나게 섞는다.")


print("=================")
make_simple_latte()
print("=================")
print("세팅 변경")
time.sleep(3)
print("=================")
make_blueberry_smoothie()
print("=================")
time.sleep(3)
make_dolcelatte()
print("=================")
make_dolcelatte()
print("=================")