fruits = ["apple","banana","charry","orange"]
#리스트 반전
fruits.reverse()
print(fruits)

#리스트 연결
vegetables = ["carrot","cucumber"]
grocery = fruits + vegetables
print(grocery)
numbers = [10,5,8,1,7]
numbers.sort()
print("numbers : ",numbers)

slice_numbers = numbers[1:4]
print("slice_numbers : ",slice_numbers)
numbers_clone = numbers[:]
print("numbers_clone : ",numbers_clone)
numbers_copy = numbers.copy()
print("numbers_copy : ",numbers_copy)