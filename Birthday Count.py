from datetime import datetime
now=datetime.now()
bday=datetime(now.year,9,22)
if bday<now:
    bday=datetime(now.year+1,9,22)
diff=bday-now
print(diff.days)
