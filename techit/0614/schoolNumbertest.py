# myGrade = 10
# yourGrade = 15

# myGrade = int(input("당신의 학번을 입력하세요 : "))
# yourGrade = int(input("다른 사람의 학번을 입력하세요 : "))

# if myGrade == yourGrade:
#     print("앗 동기네요!")
#     print("반갑습니다.")
# print("누구세요")

# print(myGrade != yourGrade)
# print(myGrade == yourGrade)
# print(myGrade > yourGrade)
# print(myGrade >= yourGrade)
# print(myGrade < yourGrade)
# print(myGrade <= yourGrade)

myGrade = int(input("당신의 학번을 입력하세요 : "))
yourGrade = int(input("다른 사람의 학번을 입력하세요 : "))

if myGrade == yourGrade:
    print("앗 동기네요!")
elif myGrade > yourGrade:
    print("안녕하세요, 선배님!")
elif myGrade < yourGrade:
    print("안녕하세요, 후배님!")
else:
    print("누구세요?")