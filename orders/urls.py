from django.urls import path

from orders.views import order_List


app_name='orders'

urlpatterns = [
    path('',order_List.as_view(),name='order_list')
    
]