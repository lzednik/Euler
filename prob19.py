__author__ = 'Lada'

import datetime

sundays=0

for year in range(1901,2001):
    for month in range(1,13):
            try:
                a= datetime.date(year,month,1).weekday()
            except:
                a="E"

            if a==6:
                sundays+=1

print "The solution is: " + str(sundays)