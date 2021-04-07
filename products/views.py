from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import *
import json
from django.db.models import Q
from django.core.paginator import Paginator

def recivedata(requset):
    if requset.user.is_authenticated:
        body=json.loads(requset.body)
        slug=body['slug']
        action=body['action']
        user=User.objects.get(username=requset.user)
        product=Product.objects.get(PRDSlug=slug)
        if action == 'add':
            order,created=OrderItem.objects.get_or_create(product=product,customer=user)
            order.quantity+=1
            order.save()
        return JsonResponse('data was submitted',safe=False)

def allorders(requset):
    if requset.user.is_authenticated:
        obj =OrderItem.objects.filter(customer=requset.user)
        return render(requset,'home_template/all_order.html',{'obj':obj})
    else:return redirect('login')


def quna(requset):
    if requset.user.is_authenticated:
        body=json.loads(requset.body)
        print('body :',body)
        action=body['action']
        orderid=body['orderId']
        order=OrderItem.objects.get(pk=orderid)
        if action == 'add':
            order.quantity+=1
            order.save()
        if action == 'remove':
            order.quantity-=1
            order.save()
            if order.quantity <=0:
                order.delete()
        return JsonResponse('data was submitted',safe=False)
    else:return redirect('login')


def addaddress(requset):
    if requset.user.is_authenticated:
        if requset.method == 'POST':
            if requset.POST['n1'] and requset.POST['n2'] and requset.POST['email'] and requset.POST['covernorate'] and requset.POST['state'] :
                phon1=str(requset.POST['n1'])
                phon2=str(requset.POST['n2'])
                email=requset.POST['email']
                covernrate=requset.POST['covernorate']
                state=requset.POST['state']
                user=User.objects.get(username=requset.user)
                order=OrderItem.objects.filter(customer=requset.user)
                x=Address.objects.create(user=user,covernorate=covernrate,state=state,phone_number1=phon1,phone_number2=phon2 ,email=email)
                for i in order :
                    i.address=x
                    i.save()
                return redirect('/')
            else:
                return HttpResponse('<script> history.back()</script>')
        return render(requset,'home_template/address.html')
    else:return redirect('login')

def mangement(requset):
    if requset.user.is_authenticated:
        data=json.loads(requset.body)
        action=data['action']
        product=data['product']
        customer=data['customer']

        product=Product.objects.get(PRDSlug=product)
        user=User.objects.get(username=customer)

        order=OrderItem.objects.filter(product=product,customer=user)
        for order in order:
            if action =='cancell':
                order.complate='Cancellation'
                order.save()
            if action == 'Postponementt':
                order.complate='Postponement'
                order.save()
            if action == 'complatt':
                order.complate='complate'
                order.save()
        print('data :',data)
        return JsonResponse('data was Submited ' ,safe=False)  
    else:return redirect('login')

   
def search_state(requset):
    if requset.user.username == 'Social':
        if requset.method =='GET':
            data=requset.GET['filter_searcg']
            filtr=OrderItem.objects.filter(complate=data)
            if not filtr :
                filtr=OrderItem.objects.filter(complate=data.lower())
                if not filtr :
                    filtr=OrderItem.objects.filter(complate=data[:1].lower())
            if data =='cancel' or data =='Cancel' or data =='cencel' or data =='الغاء' or data =='لغاء' or data =='الغأ' or data =='لغأ':
                data='Cancellation'
                filtr=OrderItem.objects.filter(complate=data)
                print('filter :',filtr)

            if data =='complate' or data =='complated' or data =='complete' or data =='complet' or data =='مكتمل' or data =='مكتملة' or data =='موكتمل' or data =='موكتملة':
                data='complate'
                filtr=OrderItem.objects.filter(complate=data)

            if data == 'postponement' or data == 'postponment' or data == 'postponemnt' or data == 'postponmnt' or data == 'تاجيل' or data == 'تأجيل' or data == 'مؤجلة' or data == 'موجلة' or data == 'مؤجل' or data == 'موجل':
                data = 'Postponement'
                filtr=OrderItem.objects.filter(complate=data)

            return render(requset,'home_template/ordersmanagement.html' ,{'obj':filtr})
    else:return redirect('login')
def search_order(requset):
        if requset.user.username == 'Social':
            if requset.method =='GET':
                data=requset.GET['filter_searcg']
                customer=User.objects.get(username=data)
                filtr=OrderItem.objects.filter(customer=customer)
            return render(requset,'home_template/ordersmanagement.html' ,{'obj':filtr})
        else:return redirect('login')

def search_date(requset):
    if requset.user.is_authenticated:
        if requset.user.username == 'Social':
            if requset.method =='GET':
                data=requset.GET['filter_searcg']
                filtr={}

            if not filtr :
                mached=[]
                all=OrderItem.objects.all()
                for date in all :
                    if str(date.date_add.date()) == data:
                        mached.append(date)
                    elif str(date.date_add.date()) == data.replace('/','-'):
                        mached.append(date)
                    
                    elif str(date.date_add.date()) == data.replace(' ','-'):
                        mached.append(date)
                        
                    elif str(date.date_add.date()) == data.replace(' ','-'):
                        mached.append(date)
                print('matched :',mached)
                filtr=mached
        return render(requset,'home_template/ordersmanagement.html' ,{'obj':filtr})
    else:
        return redirect('login')
        
        
#______main filter__________#

def main_filer(requset):
    fillter=[]
    message=''
    ss=''
    if requset.method == 'GET':
        Z=requset.GET.get('search')
        type=requset.GET.get('s')
        if Z and type == 'Electrical':
            fillter=Product.objects.filter(PRDName=Z)
            if not fillter:
                fillter=Product.objects.filter(PRDName=Z.lower())
                ss=Z.lower()
        elif Z and type == 'Carpets and meridians':
            fillter=Product.objects.filter(PRDName=Z)
            if not fillter:
                fillter=Product.objects.filter(PRDName=Z.lower())
                ss=Z.lower()
        elif Z and type == 'the games':
            fillter=Product.objects.filter(PRDName=Z)
            if not fillter:
                fillter=Product.objects.filter(PRDName=Z.lower())
                ss=Z.lower()
        elif Z and type == 'Mobile phones':
            fillter=Product.objects.filter(PRDName=Z)
            if not fillter:
                fillter=Product.objects.filter(PRDName=Z.lower())
                ss=Z.lower()
        else:
            fillter=Product.objects.filter(PRDType=type)
        if not fillter:
            message='There is no result'
       # paginator=Paginator(fillter,3)
        #page_num=requset.GET.get('page')
       # fillter=paginator.get_page(page_num)

        context={
            'obj':fillter,
            'message':message,
            'X':ss
        }
        return render(requset,'home/index.html',context)

#____sort by type_____#

def sort_by_type(requset,type):
    message=''
    fillter=Product.objects.filter(PRDType=type)
    if not fillter:
        message="There is no result"
    context={
        'obj':fillter,
        'message':message
    }
    return render(requset,'home/index.html',context)

#_________create_order______#

def create_order(requset):
    x=''
    all_product=Product.objects.all()
    if requset.method == 'POST':
        product_name=requset.POST.get('s')
        covernorate=requset.POST.get('covernorate')
        state=requset.POST.get('city')
        phone1=requset.POST.get('phoonNumber1')
        phone2=requset.POST.get('phoneNumber2')
        if not phone2:
            phone2=''
        qunatitiy=float(requset.POST.get('quantity'))
        delivery_price=float(requset.POST.get('deliveryPrice'))
        customer=requset.user.username
        employee=requset.POST.get('shippingEmployee')
        product_name=Product.objects.get(PRDSlug=product_name)
        order,create=OrderItem.objects.get_or_create(product=product_name,customer=requset.user,employee=employee,quantity=qunatitiy,delivery_price=delivery_price,)
        address=Address.objects.create(user=requset.user,covernorate=covernorate,state=state,phone_number1=phone1,phone_number2=phone2)
        order.address=address
        order.save()
        return redirect('home')
    context={
        'all_product':all_product,
    }
    return render(requset,'home/create_order.html',context)

    #___create order from product___#

def create_order_from_product(requset,slug):
    all_product=Product.objects.all()
    product=Product.objects.get(PRDSlug=slug)
    if requset.method == 'POST':
        product_name=slug
        covernorate=requset.POST.get('covernorate')
        state=requset.POST.get('city')
        phone1=requset.POST.get('phoonNumber1')
        phone2=requset.POST.get('phoneNumber2')
        if not phone2:
            phone2=''
        qunatitiy=float(requset.POST.get('quantity'))
        delivery_price=float(requset.POST.get('deliveryPrice'))
        customer=requset.user.username
        employee=requset.POST.get('shippingEmployee')
        product_name=Product.objects.get(PRDSlug=product_name)
        order,create=OrderItem.objects.get_or_create(product=product_name,customer=requset.user,employee=employee,quantity=qunatitiy,delivery_price=delivery_price,)
        address=Address.objects.create(user=requset.user,covernorate=covernorate,state=state,phone_number1=phone1,phone_number2=phone2)
        order.address=address
        order.save()
        return redirect('home')
    context={
        'obj':product,
        'all_product':all_product
    }
    return render(requset,'home/create_order.html',context)

def detail_product(requset,slug):
    obj=Product.objects.get(PRDSlug=slug)
    context={
        'obj':obj,
    }
    return render(requset,'detail_product/detail_product.html',context)