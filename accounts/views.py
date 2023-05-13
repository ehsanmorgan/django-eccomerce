from django.shortcuts import render

# Create your views here.


def sing_up(request):
   pass

def profile(request):
    return render( 'accounts/profile.html' ,{})

