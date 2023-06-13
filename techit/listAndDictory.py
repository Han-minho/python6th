information = {"고향":"수원", "취미":"영화관람", "좋아하는 음식":"국수"}
foods = ["된장찌개","피자","제육볶음"]
print("취미 : ",information.get("취미"))
information["특기"] = "피아노"
information["사는 곳"] = "서울"
del information["좋아하는 음식"]
print("전체 출력 : ",information)
print("전체 길이 : ",len(information))
# 파일 초기화
information.clear()
print("초기화 뒤 내용 : ",information)
print(foods[-2])
foods.append("김밥")
print(foods)
del foods[1]
print(foods)
# foods.pop(0)
# print(foods)

