#1
 import datetime
 x = datetime.datetime.now()
 newDate = x - datetime.timedelta(days=5)
 print(newDate.day) 10
 
#2
 import datetime
 x = datetime.datetime.now()
 Yesterday = x - datetime.timedelta(days=1)
 Tomorrow = x + datetime.timedelta(days=1)
 print("Yesterday: ", Yesterday.day)
 print("Today: ", x.day)
 print("Tomorrow: ", Tomorrow.day)
 
#3
 import datetime
 x = datetime.datetime.now().replace(microsecond=0)
 print(x) 2025-02-15 14:39:40
 
#4
 import datetime
 x = datetime.datetime.now().replace(microsecond=0)
 y = datetime.datetime(2025, 5, 6, 22, 32, 59)
 print(y-x)
