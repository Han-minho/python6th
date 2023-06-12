class CustomException(Exception):
    def __init__(self,message):
        self.message = message

# error 발생함수
try :
    raise CustomException("This is a custom exception.")
except CustomException as e:
    print(f"Error : {e.message}")
    