#피보나치 수열
def fibonacci(n):
    a,b = 0,1
    for _ in range(n):
        yield a
        a,b = b, a + b

result = fibonacci(10)

print(next(result))
print(next(result))
print(next(result))
for num in result :
    print(num)