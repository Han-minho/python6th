# 파일 읽기
# file_object = open('example.txt', 'r')
#
# content = file_object.read()
#
# print(content)
#
# file_object.close()

# 파일 쓰기
# file_object1 = open('new_example.txt','w')
# content = "This in a new file.\nPython is fun!"
#
# file_object1.write(content)
#
# file_object1.close()

#파일 위치 위치 확인 및 변경
# print("파일 open")
# file_object2 = open('new_example.txt','r')
#
# print("현재 파일 위치 확인")
# position = file_object2.tell()
# print("파일 위치 : ",position)
# print("파일 포인터 위치 변경")
# file_object2.seek(7)
# print("변경 위치 확인")
# position = file_object2.tell()
# print("New positioin : ",position)
# file_object2.close()

#파일 쓰기
# with open('example.txt', 'w') as file_object:
#     content = """This is a multiline string
# Python is a versatile language.
# It is easy to learn and use."""
#     print(content)
#     file_object.write(content)

#공백 제거
# with open('example.txt', 'r') as file_object:
#     lines = file_object.readlines()
#
#     for line in lines:
#         print(">",line.strip())

