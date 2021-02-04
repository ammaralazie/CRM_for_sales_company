from.models import OrderItem
import datetime
import dateutil.parser

def allorders(request):
    count=0
    if request.user.is_authenticated:
        obj=OrderItem.objects.filter(customer=request.user)
        for i in obj:
            count +=i.quantity
    return{'all':count}

def everyorder(request):
    obj=0
    countCa=0
    countCo=0
    countPo=0
    if request.user.is_authenticated:
        obj2=OrderItem.objects.all()
        for fillter in obj2:
            if fillter.address :
                if fillter.complate :
                    obj+=1
                if fillter.complate == 'complate':
                    countCo+=1
                elif fillter.complate == 'Cancel':
                    countCa+=1
                elif fillter.complate =='Postponement':
                    countPo+=1

    return{'everyorder':obj ,'countPo':countPo,'countCo':countCo,'countCa':countCa}

def maxorders(request):
    allorder=OrderItem.objects.all()
    dateNow=datetime.datetime.now()
    filter=''
    enddate=''
    
    complets=[]
    print('dateNow :',dateNow)
    print('enddate :',enddate)
    for i in range(360):
        obj=[]
        
        listcount=[]
        enddate=dateNow-datetime.timedelta(days=1)
        filter=OrderItem.objects.filter(date_add__range=[enddate.strftime('%Y-%m-%d %H:%M:%S'),dateNow.strftime('%Y-%m-%d %H:%M:%S')])
        dateNow=enddate
        for j in filter:
            if j.complate == 'complate' :
                obj.append(j)
        complets.append(obj)
    for i in complets:
        count=0
        for j in i:
            count+=1
        listcount.append(count)
    m=0
    bmea=[]
    
    m=max(listcount)
    for i in range(7):
        x=listcount[i]/m
        x=x*100
        bmea.append(float(x))
    


    return {'max':m,'s':bmea,'count':listcount}


                


