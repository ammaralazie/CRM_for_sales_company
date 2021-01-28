from django.urls import path
from .views import *

app_name='products'

urlpatterns = [
    path('encrement/',recivedata,name='recivedata'),
    path('Orders/',allorders,name='allorders'),
    path('qunatity/',quna,name='quna'),
    path('address/',addaddress,name='addaddress'),
    path('mangement/',mangement,name='mangement'),
    path('state/',search_state,name='search_state'),
    path('order/',search_order,name='search_order'),
    path('date/',search_date,name='search_date'),    
]