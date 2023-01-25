from django.urls import path


app_name='product'

from .views import productList,productDetail

urlpatterns = [
    path('',productList. as_view(),name='product_list'),
    path('<slug:slug>',productDetail.as_view(),name='product_detail')
]
