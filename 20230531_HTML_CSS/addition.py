#두 정수를 더하는 함수
def add(a,b):
    return a+b

def print_result(a,b,sum):
    print(f"Sum of {a} and {b} is : {sum}")

#메인함수
def main():
    #두 정수를 입력받음
    a = int(input("Enter first integer : "))
    b = int(input("Enter second integer : "))

    #덧셈 함수 호출
    sum = add(a,b)

    #결과 출력
    print_result(a,b,sum)

if __name__ == "__main__":
    main()