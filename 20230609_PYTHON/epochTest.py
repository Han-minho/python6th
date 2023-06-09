# epoch 실습
# import time
# print(time.time())
# print(time.ctime())

import time
from datetime import datetime
from datetime import date

dt = datetime(year=2023,month=5,day=5,hour=10,minute=30)
print(dt)
print(type(dt))

current_datetime = datetime.now()
print(current_datetime)

d = date(year=2023,month=6,day=25)
print(d)

current_date = date.today()
print(current_date)

