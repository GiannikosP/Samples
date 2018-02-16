import datetime
now=datetime.datetime.now()

year=now.year
month=now.month
day=now.day
weekday=datetime.datetime.today().weekday()
count=0
for i in range (year,year+10):
	for j in range (month,12):
		if (datetime.datetime(i,j,day).weekday()==weekday):
			count=count+1
	month=1
print count