from django.shortcuts import render,redirect
from.models import Profile,ContactNumber,Adresse
from.forms import SingupForm,Activatecode
from django.core.mail import send_mail
from django.contrib.auth.models import User
from product.models import product,Brand,reviews
from orders.models import order

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
            code = form.cleaned_data['code']
            if len(code) == 12:

                if code == profile.code:
                    profile.code = ''
                    profile.save()
                return redirect('/accounts/activated')
        
    else:
        form=Activatecode()
    return render(request,'activate.html',{'form':form})
  

def profile(request):
    myprofile=Profile.objects.all()
    profile=Profile.objects.get(user =request.user)
    adresse=Adresse.objects.filter(user=request.user)
    contactnumber=ContactNumber.objects.filter(user=request.user)
    return render(request,'profile.html',{ 'myprofile':myprofile,'profile':profile,'adresse':adresse,'contactnumber':contactnumber})



def activated(request):
    
    return render(request,'activated.html',{})


def dashbord(request):
    user=User.objects.all().count()
    products=product.objects.all().count()
    brand=Brand.objects.all().count()
    review=reviews.objects.all().count()
    orders=order.objects.all().count()
    
    recevied=order.objects.filter(order_status='Recevied').count()
    processed=order.objects.filter(order_status='Processed').count()
    shipped=order.objects.filter(order_status='Shipped').count()
    delivered=order.objects.filter(order_status='Delivered').count()

    
    return render(request,'dashbord.html',{
        'user':user,
        'products':products,
        'brand':brand,
        'review':review,
        'orders':orders,
        
        'recevied':recevied,
        'processed':processed,
        'shipped':shipped,
        'delivered':delivered
        
        
    })
    
    
    
    
    
from .tasks import send_bulid_emails

def test_send(request):
    send_bulid_emails.delay(5)
    return render(request,'test_celery.html',{})
    