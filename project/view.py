from django.shortcuts import render,redirect
from django.http import HttpResponse
from products.models import Product,OrderItem
from datetime import timedelta
import datetime
from django.contrib.auth import login,authenticate
from .forms import SignUpForm
from django.db.models import Q
import dateutil.parser
from .utils import date_list

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
    time=''
    print('method ;',requset.method)
    if requset.method == 'POST':
        time=requset.POST['time']
    _date=[]
    reportDate=date_list(time)
    context={
        'd':_date,
        'reportDate':reportDate ,
        'time':time,

        'st':'start',
        'en':'end',

        'com':'complate',
        'Can':'Cancellation',
        'Pos':'Postponement',
        'al':'all'

    }
    return render(requset,'home_template/admin_page.html',context) 

#__________admin filter date __________#     

def admin_filter(requset,time,d):
    #dd=''
   # for i in range(10):
   #     dd+=d[i]
   # if dd:
   #     datee=datetime.datetime.strptime(dd,'%Y-%m-%d').date()
   # week=d-timedelta(days=7)
    
    coverttodate=''
    enddate=''
    convertDate=''
    endDate=''
    fillter=''
    if time == 'week':
        timusa=dateutil.parser.parse(d)
        coverttodate=timusa
        enddate=dateutil.parser.parse(d)-timedelta(days=6) 
        convertDate=datetime.datetime.combine(datetime.datetime.date(enddate),datetime.datetime.time(dateutil.parser.parse('00:00:00'))) 
        endDate=datetime.datetime.combine(datetime.datetime.date(coverttodate),datetime.datetime.time(dateutil.parser.parse('23:59:59'))) 
        fillter=OrderItem.objects.filter(date_add__range=[convertDate,endDate])
    if time == 'day':
        coverttodate=dateutil.parser.parse(d)
        timusa=coverttodate-timedelta(hours=3)
        coverttodate=timusa.strftime('%Y-%m-%d %H:%M:%S')
        enddate=dateutil.parser.parse(coverttodate)-timedelta(hours=1)
        enddate=enddate.strftime('%Y-%m-%d %H:%M:%S')
        fillter=OrderItem.objects.filter(date_add__range=[enddate,coverttodate])
    
    if time == 'date':
        timusa=dateutil.parser.parse(d)
        coverttodate=timusa
        enddate=dateutil.parser.parse(d)-timedelta(days=30) 
        convertDate=datetime.datetime.combine(datetime.datetime.date(enddate),datetime.datetime.time(dateutil.parser.parse('00:00:00'))) 
        endDate=datetime.datetime.combine(datetime.datetime.date(coverttodate),datetime.datetime.time(dateutil.parser.parse('23:59:59'))) 
        fillter=OrderItem.objects.filter(date_add__range=[convertDate,endDate])

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
            elif i.complate == 'Cancellation':
                countCanel+=1
            elif i.complate =='Postponement':
                countPostpon+=1
    reportDate=date_list(time)

    context={
        'reportDate':reportDate,
        'countCanel':countCanel,
        'countComplate':countComplate,
        'countPostpon':countPostpon,
        'counttotalorders':counttotalorders,
        'coverttodate':timusa+timedelta(hours=3),
        'time':time,

        #this use as argument for admin_without_filter
        'st':convertDate,
        'en':endDate,

        'com':'complate',
        'Can':'Cancellation',
        'Pos':'Postponement',
        'al':'all'

    }
    return render(requset,'home_template/admin_page.html',context) 

def admin_without_filter(request,st,en,com):
    listitem=[]
    if st == 'start' and en == 'end':
        fillterr=OrderItem.objects.all()
    else:
        fillterr=OrderItem.objects.filter(date_add__range=[st,en])
    if com == 'Cancellation':
        for i in fillterr:
            if i.complate == 'Cancellation':
                listitem.append(i)

    if com == 'complate':
        for i in fillterr:
            if i.complate == 'complate':
                listitem.append(i)
    if com == 'all':
         for i in fillterr:
            listitem.append(i)

    if com == 'Postponement':
        for i in fillterr:
            if i.complate == 'Postponement':
                listitem.append(i)
    context={
        'obj':listitem
    }
    
    return render(request,'admin_pages_without_main/theorders.html',context)


