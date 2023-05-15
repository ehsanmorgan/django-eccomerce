from django.urls import path
from .views import sing_up,profile,dashbord,activate_code

app_name='accounts'

urlpatterns = [
    path('signup/', sing_up, name='signup'),
    path('profile/',profile,name='profile'),
    path('<str:username>/activate',activate_code,name='activate'),
    path('dashbord/',dashbord,name='dashbord'),
    
]
