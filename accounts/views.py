from django.shortcuts import render
from.models import Profile

# Create your views here.


def sing_up(request):
   pass

def profile(request):
    
    return render(request,'profile.html',{})

