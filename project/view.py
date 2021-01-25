from django.shortcuts import render,redirect, get_object_or_404
from products.models import Product,OrderItem

from django.contrib.auth import login,authenticate
from .forms import SignUpForm

def home(request):
    obj=Product.objects.all()
    context={'obj':obj}
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

def detail(request ,id):
    order=OrderItem.objects.get(id=id)
    return render(request,'home_template/detail.html',{'obj':order})
        