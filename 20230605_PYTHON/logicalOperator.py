# 논린 AND
a = 5
b = 2
c = 3
d = 200

print("*********Logical and ***********")
print("a > b and a > c : ",a > b and a > c)
print("a > b and a < c : ",a > b and a < c)
print("a < b and a > c : ",a < b and a > c)
print("a < b and a < c : ",a < b and a < c)
print("a > b and c : ",a > b and c)
print("a > b and c and d : ",a > b and c and d)
print("a < b and c : ",a < b and c)
print("a < b and c and d : ",a < b and c and d)

# 논리 OR
print("*********Logical OR ***********")
print("a > b or a > c : ",a > b or a > c)
print("a > b or a < c : ",a > b or a < c)
print("a < b or a > c : ",a < b or a > c)
print("a > b or c : ",a > b or c)
print("a > b or c or d : ",a > b or c or d)
print("a < b or c : ",a < b or c)
print("a < b or c or d : ",a < b or c or d)

#논리 NOT
print("*********Logical NOT ***********")
print("not(a < b) : ",not(a < b))
print("not(a > b) : ",not(a > b))