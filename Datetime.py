from datetime import datetime
print(datetime.now())
print(datetime(2024,12,3)-datetime.now())
diff=datetime(2024,12,3)-datetime.now()
print(diff.days)
now=datetime.now()
print(now.year,now.day)


