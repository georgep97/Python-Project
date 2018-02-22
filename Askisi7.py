import datetime

today = datetime.date.today()

print "Today's date: ",today
dayofcurrentweek = today.isoweekday()
def up(day, years):
    try:
        return day.replace(year = day.year + years)
    except ValueError:
        return day + (date(day.year + years, 1, 1) - date(day.year, 1, 1))
counter=0
for i in range(1,11):
    result = up(today,i)
    dayofweek = result.isoweekday()
    if dayofweek == dayofcurrentweek:
        counter+=1
        if counter==1:
            print "Same Weekdate as Today Dates"
        print result
if counter > 0:
    print "Number of same Dates:",counter
else:
    print "No same dates"
