from django.urls import path

from orders.views import order_List,add_to_cart,remover_from_cart,chekout,invoice
from .api import orderListAPI,cartdetailAPI,createorder


app_name='orders'

urlpatterns = [
    path('',order_List.as_view(),name='order_list'),
    path('add_to_cart',add_to_cart,name='add_to_cart'),
    path('remover_from_cart/<int:id>',remover_from_cart,name='remover_from_cart'),
    path('chekout',chekout,name='chekout'),

    
    
    
    
    
    #api
    path('order/<str:username>/create_list',createorder.as_view()),
    path('order/<str:username>/list',orderListAPI.as_view()),
    path('cart/<str:username>/list',cartdetailAPI.as_view()),
   
    
]