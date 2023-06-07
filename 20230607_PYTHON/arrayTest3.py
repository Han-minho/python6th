# 문자열 함수 비교
s = "       hello world          "
print(s.upper())
print(s.lower())
# swapcase(대소문자 반전)
print(s.swapcase())
print(s.title())

#대소문자 감별
print(s.isupper())
print(s.islower())

#공백 감별, 숫자 존재 감별
print(s.istitle())
print(s.isdigit())
print("=============")
print(s.lstrip())
print(s.rstrip())
print(s.strip())