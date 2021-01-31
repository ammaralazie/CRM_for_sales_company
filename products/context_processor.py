from.models import OrderItem
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