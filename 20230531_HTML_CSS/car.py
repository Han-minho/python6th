class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.speed=0

    def accelerate(self):
        self.speed+=5

    def brake(self):
        self.speed-=5

# 객체 생성
my_car = Car("Toyota" , "Camry" , 2020)

# 객체의 메서드 사용
my_car.accelerate()
my_car.accelerate()
my_car.brake()

# 객체의 속성 사용
current_speed = my_car.year()
print(f"{my_car.make}{my_car.model}({my_car.year}) is going {current_speed} mph.")