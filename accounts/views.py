from django.shortcuts import render
from.models import Profile

# Create your views here.


def sing_up(request):
   pass

def profile(request):
    profile=Profile.objects.get(user =request.user)
    return render(request,'profile.html',{'profile':profile})

