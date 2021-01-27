from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import *
import json

def recivedata(requset):
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
    obj =OrderItem.objects.filter(customer=requset.user)
    return render(requset,'home_template/all_order.html',{'obj':obj})


def quna(requset):
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


def addaddress(requset):
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

def mangement(requset):
    data=json.loads(requset.body)
    action=data['action']
    product=data['product']
    customer=data['customer']

    product=Product.objects.get(PRDSlug=product)
    user=User.objects.get(username=customer)

    order=OrderItem.objects.get(product=product,customer=user)
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

   
