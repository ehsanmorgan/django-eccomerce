from django.urls import path

from orders.views import order_List
from .api import orderListAPI,cartdetailAPI


app_name='orders'

urlpatterns = [
    path('',order_List.as_view(),name='order_list'),
    
    
    
    
    
    #api
    path('order/list',orderListAPI.as_view(),name='orderlist'),
    path('cart/<str:username>/list',cartdetailAPI.as_view(),name='cartlist')
    
]