from django.urls import path


app_name='product'

from .views import productList,productDetail,brand_list,brand_detail,query_debug


urlpatterns =[
    path('debug',query_debug,name='query_debug'),
    path('',productList. as_view(),name='product_list'),
    path('<slug:slug>',productDetail.as_view(),name='product_detail'),
    path('brands/',brand_list.as_view(),name='brand_list'),
    path('brands/<slug:slug>',brand_detail.as_view(),name='brand_detail'),
    
]
