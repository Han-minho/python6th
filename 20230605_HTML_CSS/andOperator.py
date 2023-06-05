def function1():
    print("Function 1 is executed.")
    return True

def function2():
    print("Function 2 is executed.")
    return False

# 참 and function1() and function2()
result1 = True and function1() and function2()
print("True and function1() and function2();",result1)

result2 = False and function1() and function2()
print("False and function1() and function2();",result2)