from django.urls import path

from orders.views import order_List
from .api import orderListAPI,cartdetailAPI,createorder


app_name='orders'

urlpatterns = [
    path('',order_List.as_view(),name='order_list'),
    
    
    
    
    
    #api
    path('order/<str:username>/create_list',createorder.as_view()),
    path('order/<str:username>/list',orderListAPI.as_view()),
    path('cart/<str:username>/list',cartdetailAPI.as_view()),
   
    
]