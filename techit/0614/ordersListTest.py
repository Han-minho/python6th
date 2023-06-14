# 주문 하기 코드
# orders = ["짜장","짬뽕","탕수육"]

# 주문 추가
# orders.append("냉면")
# orders.insert(1,"냉면")
# orders.insert(3,"양장피")
# print(orders)

# 원하는 자리의 내용을 삭제
# 주문 삭제 1
# del orders[0]
# print(orders)

#주문 삭제 2
# orders.remove("짬뽕")
# print(orders)

# print(len(orders))
# 문자열 갯수 조회
# name = "안녕하세요 코드라이언입니다."
# print(len(name))
# num = [20,40,50,10,30]
# print(num)

# numList = [2,7,9,8,1]
# addition = numList[0]+numList[1]+numList[2]+numList[3]+numList[4]
# add = sum(numList)
# print(numList)
# print(add)
# numDigit = [20,40,50,10,30]
# addition = sum(numDigit)
# total = addition / len(numDigit)
# print(total)

# 최대값과 최소값
# print(max(numDigit))
# print(min(numDigit))

# 딕셔너리
# family = {"아빠":45,"엄마":49,"나":22}
# print(family)

menu = {"짜장":4000,"짬뽕":5000,"탕수육":9000}

# menu["냉면"] = 6000
print(menu["짜장"])
print(menu["탕수육"])
# print(menu)
menu["탕수육"] = 8500
menu["순대국"] = 8000
menu["짱뽕"] = 5000
print(menu)
print(menu["짜장"],menu["탕수육"])
del menu["짜장"]
del menu["탕수육"]
print(menu)