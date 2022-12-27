from datetime import datetime 
now= datetime.now()
then = datetime(1996, 2, 3)
delta=now - then
#calculate time differences
print(delta.days)
print(delta.seconds)

