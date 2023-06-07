#배열 생성 및 원소 접근
import array
stu_roll = array.array('i',[101,102,103,104,105])
print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])

print("for in 사용")
for element in  stu_roll:
    print(element)

#index를 이용한 구문
print("index 이용한 순회")
n = len(stu_roll)
for i in range(n):
    print(i,"=",stu_roll[i])

#while문
print("while문 index를 사용한 while문 배열 순회")
i = 0
while i < n:
    print(stu_roll[i])
    i += 1

