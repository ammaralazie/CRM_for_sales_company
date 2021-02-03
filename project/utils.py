from datetime import timedelta
import datetime
def date_list(time):
    reportDate=[]
    if time == 'week':
        d=datetime.datetime.now()
        d=datetime.datetime.now()
        for i in range(8):
            reportDate.append(d)
            d-=timedelta(days=7)
    if time == 'day':
        d=datetime.datetime.now()+timedelta(hours=3)
        for i in range(24): 
            reportDate.append(d)
            d-=timedelta(hours=1)
    if time == 'date':
        d=datetime.datetime.today()
        for i in range(12): 
            reportDate.append(d)
            d-=timedelta(days=30)
    return reportDate