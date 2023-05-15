from django.shortcuts import render
from.models import Profile,ContactNumber,Adresse
from.forms import SingupForm,Activatecode

# Create your views here.


def sing_up(request):
    
    if request.method=='POST':
        form=SingupForm(request.POST)
        
    else:
        
        form=SingupForm()
        
    return render(request,'signup.html',{'form':form})



def activate_code(request):
    pass
  

def profile(request):
    profile=Profile.objects.get(user =request.user)
    adresse=Adresse.objects.filter(user=request.user)
    contactnumber=ContactNumber.objects.filter(user=request.user)
    return render(request,'profile.html',{'profile':profile,'adresse':adresse,'contactnumber':contactnumber})

def dashbord(request):
    pass