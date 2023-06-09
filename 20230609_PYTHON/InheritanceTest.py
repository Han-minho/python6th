# 상속
class Mobile:
    fp = 'yes'

readlme = Mobile()
redme = Mobile()
geek = Mobile()

print("===========================")
print("Mobile : ",Mobile.fp)
print("readlme : ",readlme.fp)
print("redme :",redme.fp)
print("geek : ",geek.fp)

Mobile.fp = 'no'

print("===========================")
print("readlme : ",readlme.fp)
print("redme :",redme.fp)
print("geek : ",geek.fp)
print("===========================")
readlme.fp = "Not Working"
print("Mobile : ",Mobile.fp)
print("readlme : ",readlme.fp)
print("redme :",redme.fp)
print("geek : ",geek.fp)
print("===========================")

