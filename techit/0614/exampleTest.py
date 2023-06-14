# for x in range(5):
#     for y in range(5):
#         print("*",end="")
#     print("")
#
# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print("")

# for x in range(5):
# print("*")

# for x in range(5,0,-1):
#     print(x)


# 별이 빛나는 밤 문제 해설

# num = int(input("증가할 숫자를 입력하세요 : "))
# for x in range(5):
#     print("*"*5)
#
# for x in range(num):
#     print("*"*(x+1))

# 줄 바꿔 출력하기
# x = int(input("숫자를 입력하세요 : "))
# for i in range(x,0,-1):
#     print(i)

# y = int(input("숫자를 입력해주세요 : "))
# for i in range(y):
#     if i % 10 == 0:
#         print("")
#     print(i+1,end="\t")
# print()

# 오늘의 당첨 번호(lotto)

# import random
#
# count = int(input("로또를 몇개 구매하시겠습니까? : "))
#
#
# for i in range(count):
#     lotto = random.sample(range(1, 46), 6)
#     lotto.sort()
#     print(lotto)
# print("lotto finsh!!!")

for i in range(9):
    print(i)