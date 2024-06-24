from datetime import datetime
from datetime import timedelta
n=0
i=datetime.now()
while(i<datetime(2024,6,10)):
      print(i)
      n=n+1
      i=i+timedelta(days=3*n)
       
