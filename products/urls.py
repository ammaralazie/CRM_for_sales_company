from django.urls import path
from .views import *

app_name='products'

urlpatterns = [
    path('encrement/',recivedata,name='recivedata'),
    path('Orders/',allorders,name='allorders'),
    path('qunatity/',quna,name='quna'),
    path('address/',addaddress,name='addaddress'),
    path('mangement/',mangement,name='mangement'),
]