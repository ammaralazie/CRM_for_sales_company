from django.shortcuts import render,redirect, get_object_or_404
from products.models import Product,OrderItem
from datetime import timedelta
import datetime
from django.contrib.auth import login,authenticate
from .forms import SignUpForm
from django.db.models import Q
import dateutil.parser

def home(request):
    obj=Product.objects.all()
    context={'obj':obj}
    d=datetime.datetime.now()-timedelta(days=7)
    while d<= datetime.datetime.now():
        print('datetime : ',d.date())
        d+=timedelta(days=1)
    return render(request,'home/index.html',context)



#__________________#

def signup(request):
    try :
        if request.method == 'POST':
            form=SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username=form.cleaned_data.get('username')
                password=form.cleaned_data.get('password1')
                user=authenticate(password=password,username=username)
                login(request,user,backend='django.contrib.auth.backends.ModelBackend')
                return redirect('/')
            return render(request,'registration/signup.html',{'form':form})
        else:
            form=SignUpForm()
            return render(request,'registration/signup.html',{'form':form})
    except :
        form=SignUpForm()
        return render(request,'registration/signup.html',{'form':form ,'note':'Something is not right, try again'})


def management(requset):
    if requset.user.is_authenticated:
        if requset.user.username == 'Social':
            obj=OrderItem.objects.all()
            return render(requset,'home_template/ordersmanagement.html' ,{'obj':obj})
    else: return redirect('login')

def detail(request ,id):
    if request.user.is_authenticated and request.user.username == 'Social':
        order=OrderItem.objects.get(id=id)
        return render(request,'home_template/detail.html',{'obj':order})
    else: return redirect('login')

#_______admin_management____________#

def admin_management(requset):
    _date=[]
    reportDate=[]
    d=datetime.datetime.now()
    for i in range(8):
        reportDate.append(d)
        d-=timedelta(days=7)
    return render(requset,'home_template/admin_page.html',{'d':_date,'reportDate':reportDate}) 

#__________admin filter date __________#     

def admin_filter(requset,d):
    #dd=''
   # for i in range(10):
   #     dd+=d[i]
   # if dd:
   #     datee=datetime.datetime.strptime(dd,'%Y-%m-%d').date()
   # week=d-timedelta(days=7)
    coverttodate=dateutil.parser.parse(d)
    enddate=dateutil.parser.parse(d)-timedelta(days=6) 
    convertDate=datetime.datetime.combine(datetime.datetime.date(enddate),datetime.datetime.time(dateutil.parser.parse('00:00:00'))) 
    endDate=datetime.datetime.combine(datetime.datetime.date(coverttodate),datetime.datetime.time(dateutil.parser.parse('23:59:59'))) 
    fillter=OrderItem.objects.filter(date_add__range=[convertDate,endDate])
    print(fillter)
    
    countCanel=0
    countComplate=0
    countPostpon=0
    counttotalorders=0

    for i in fillter:
        if i.address:
            if i.complate:
                counttotalorders+=1
            if i.complate == 'complate':
                countComplate+=1
            elif i.complate == 'Cancel':
                countCanel+=1
            elif i.complate =='Postponement':
                countPostpon+=1
    reportDate=[]
    d=datetime.datetime.now()
    for i in range(8):
        reportDate.append(d)
        d-=timedelta(days=7)
    context={
        'reportDate':reportDate,
        'countCanel':countCanel,
        'countComplate':countComplate,
        'countPostpon':countPostpon,
        'counttotalorders':counttotalorders,
        'coverttodate':coverttodate,
        'fillter':fillter,
    }
    return render(requset,'home_template/admin_page.html',context) 