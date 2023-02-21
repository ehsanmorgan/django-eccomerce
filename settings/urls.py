from django .urls import path

from .views import home

app_name='settings'



urlpatterns = [

    path('',home,name='home')
    
]

