class Vector(object) :
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #연산자 오버로딩
    # 보모의 내용을 받아 본인 객체를 재정의
    def __add__(self, other):
            return Vector(self.x + other.x, self.y + other.y)

    #부모의 내용을 받아 보모내용을 다시 정의
    def __str__(self):
        return f'Vector({self.x},{self.y})'

a = Vector(1,2)
b = Vector(3,4)
print(a)
print(b)

c = a + b
print(c)

