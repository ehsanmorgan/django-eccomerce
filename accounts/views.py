from django.shortcuts import render,redirect
from.models import Profile,ContactNumber,Adresse
from.forms import SingupForm,Activatecode
from django.core.mail import send_mail

# Create your views here.



def sing_up(request):
    
    if request.method=='POST':
        form=SingupForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            form.save()
            
            profile=Profile.objects.get(user__username=username)

            
            send_mail(
                "Activate Your Accounts",
                f"Welcome {username}\n use this code{profile.code}to activate your accounts \n green store ",
                "ehsanmorgan1994@gmail.com",
                [email],
                fail_silently=False,
            )
            
            return redirect(f'/accounts/{username}/activate')
            
        
    else:
        
        form=SingupForm()
        
    return render(request,'signup.html',{'form':form})



def activate_code(request,username):
    profile=Profile.objects.get(user__username=username)
    if request.method == 'POST':
        form=Activatecode(request.POST)
        if form.is_valid():
            code=form.cleaned_data['code']
            if code == profile.code:
                profile.code = ''
                profile.save()
                return redirect('/accounts/login/')
        
    else:
        form=Activatecode()
    return render(request,'activate.html',{'form':form})
  

def profile(request):
    profile=Profile.objects.get(user =request.user)
    adresse=Adresse.objects.filter(user=request.user)
    contactnumber=ContactNumber.objects.filter(user=request.user)
    return render(request,'profile.html',{'profile':profile,'adresse':adresse,'contactnumber':contactnumber})






def dashbord(request):
    pass