from .models import Cart,cart_detail

def get_or_create(request):
    if request.user.is_authenticated:
        cart,created=Cart.objects.get_or_create(user=request.user,cart_status='Inprogress')
        if not created:
            cart_detail1=cart_detail.objects.filter(cart=cart)
            return{'cart':cart,'cart_detail1':cart_detail1}
        return{'cart':cart}
    else:
        return{}
    
    