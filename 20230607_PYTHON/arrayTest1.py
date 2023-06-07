from array import *
# import array
stu_roll = array('i',[101,102,103,104,105])
n = len(stu_roll)
i = 0
# while i < n:
#     print(stu_roll)
#     i += 1
#
# print("Array After Insert")
# stu_roll.insert(1,106)
# stu_roll.insert(3,107)
# n = len(stu_roll)
# i = 0
# while i < n:
#     print(stu_roll[i])
#     i += 1
#
# print("array element remove")
#
# stu_roll.remove(107)
# n = len(stu_roll)
# i = 0
# while i < n:
#     print(stu_roll)
#     i += 1
#
#
# print("array element pop")
#
# stu_roll.pop(2)
# n = len(stu_roll)
# i = 0
# while i < n:
#     print(i,stu_roll)
#     stu_roll.pop()
#     i += 1
#
# print(stu_roll)

# print('array index test')
# print(stu_roll.index(104))
# print("extend() 메소드")
# arr = array('i',[201,208,209])
# stu_roll.extend(arr)
# n = len(stu_roll)
# while i < n:
#     print(stu_roll)
#     i += 1

print("reverse()메소드")
stu_roll.reverse()
n = len(stu_roll)
i = 0
while i < n:
    print(stu_roll[i])
    i += 1