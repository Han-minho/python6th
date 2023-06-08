def pw(x,y):
    z  = x ** y
    print(z)

def show(name,age):
  print(f"Name : {name} Age : {age}")
pw(2,5)
pw(y=5,x=2)
# pw(5,2,3)
show(name="멋쟁이사자",age=33)
show(age=33,name="멋쟁이사자")