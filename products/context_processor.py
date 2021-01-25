from.models import OrderItem
def allorders(request):
    count=0
    if request.user.is_authenticated:
        obj=OrderItem.objects.filter(customer=request.user)
        for i in obj:
            count +=i.quantity
    return{'all':count}