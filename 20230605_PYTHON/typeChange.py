#type conversion
a = 5
b = 2
value = a/ b
print("a / b : ",value)
print("a/ b : ",type(value))
x = 10
y = 5.5
total = x + y
print(total)
print(type(total))

j = "Hello "
k = "멋쟁이 사자"
p = j + k
print(p)
print(type(p))

q = 20
u = " 10"
r = str(q) + u  ##문자열 숫자 연산 불가
print(r)

m = 20
n = ' 멋쟁이 사자'  ##문자열 숫자 연산 불가
t = str(m) + n
print(t)

# 명시적 타입 변환
a = 5
b = 2
value = a / b
print(type(value))
int_value = int(value)

print(int_value,type(int_value))


#명시적 타입 변환
q = 20
u = '10'
print(type(u))
r = q + int(u)
print(r,type(r))

#암시적 타입 변환
q = 20
u = '10'
print(type(u))
r = str(q) + u
print(r,type(r))

# 부동소수점 타입변환
n1 = 10.99
vn1 = int(n1)

print(vn1,type(vn1))

# 복소수 변환
n1 = 10
vn1 = complex(n1)

print(vn1,type(vn1))