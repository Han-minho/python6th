from array import *
# import array
stu_roll = array('i',[101,102,103,104,105,106,107])
# n = len(stu_roll)
# i = 0

# slice문
print("배열 슬라이스")
# print(stu_roll[1:5])
# print(stu_roll[-2:])

n = len(stu_roll)

for i in range(n):
    print(i,"=",stu_roll[i])

print("1:5까지 출력")
a = stu_roll[1:5]
for i in a:
    print(i)

print("0번째부터 끝까지")
b = stu_roll[0:]
for i in b:
     print(i)

print("처음부터 5번째까지")
c = stu_roll[:5]
for i in c:
    print(i)

print("마지막 요소 4개 출력")
d = stu_roll[-4:]
for i in d:
    print(i)

print("0부터 6번째 index 까지 2씩 증가 출력")
e = stu_roll[0:7:2]
for i in e:
    print(i)

print("마지막 5개 요소 출력하다가 "
      "-[-5(-3)] = (-2) 오른쪽으로부터 "
      "2개의 요소 출력")
f = stu_roll[-5:-3]
for i in f:
    print(i)

str1 = 'LikeLion'
str2 = "LikeLion"
str3 = '''
동해물과 백두산이
마르고 닳도록
하느님이 보우하사
우리나라 만세
'''
str4 = ""'''
동해물과 백두산이
마르고 닳도록
하느님이 보우하사
우리나라 만세
'''""
str5 = 'Hello "Like Lion" How are you'
str6 = "Hello 'Like Lion' How are you"

str7 = "Hello \nHow are you?"
str8 = "Hello \nHow are \\t you?"
str9 = "Hello \How are \t you?"


print(str1)
print(str2)
print(str3)
print(str4)
print(str5)
print(str6)
print(str7)
print(str8)
print(str9)