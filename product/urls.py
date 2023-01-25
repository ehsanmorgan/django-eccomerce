from django.urls import path


app_name='product'

from .views import productList,productDetai

urlpatterns = [
    path('',productList. as_view(),name='productList'),
    path('<slug:slug>',productDetai.as_view(),name='productDetai')
]
