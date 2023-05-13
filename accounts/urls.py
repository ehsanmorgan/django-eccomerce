from django.urls import path
from .views import sing_up,profile

app_name='accounts'

urlpatterns = [
    path('signup/', sing_up, name='signup'),
    path('profile/',profile,name='profile'),
    
]
