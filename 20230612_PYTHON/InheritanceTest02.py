class Engine:
    def start(self):
        return "Engine started"
    def stop(self):
        return "Engine stopped"

class Wheels:
    def rotate(self):
        return "Wheels are rotating"

#다중 상속
class Car(Engine,Wheels):
    pass
    # def rotate(self):
    #     return super().rotate()

#안스턴스 생성
my_car = Car()

#부모 클래스의 메소드 사용
print(my_car.start())  # 출력 : Engine started
print(my_car.rotate()) # 출력 : Wheels are rotating
