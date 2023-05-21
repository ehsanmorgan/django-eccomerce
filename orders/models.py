from django.db import models
from django.utils import timezone
from product.models import product
from django.contrib.auth.models import User
from .utils.genirite_code import genirite_code
from django.utils.translation import gettext_lazy as _

# Create your models here.




CART_STATUS=(
    ('Inprogress','Inprogress'),
    ('Completed','Completed'),
    
)

class Cart(models.Model):
    
    user=models.ForeignKey(User,verbose_name=_('Cart'),related_name='user_cart',on_delete=models.SET_NULL,null=True,blank=True)
    cart_status=models.CharField(verbose_name=_('cart_status'),max_length=12,choices=CART_STATUS,default='Inprogress')
    
    def total_cart(self):
        total=0
        for product in self.cart_detail.all():
            total += product.total
        return round(total,2)
        
            




class cart_detail(models.Model):
    cart=models.ForeignKey( Cart,verbose_name=_('cart'),related_name='cart_detail',on_delete=models.CASCADE)
    product=models.ForeignKey(product,verbose_name=_('product'),related_name='cart_product',on_delete=models.SET_NULL,null=True,blank=True)
    price=models.FloatField(_('price'),null=True,blank=True)
    quantity=models.IntegerField(_('quantity'),default=1)
    total=models.FloatField(_('total'), null=True,blank=True)



    def __str__(self):
        return str(self.product)


    #def save(self, *args, **kwargs):
        #self.total= self.quantity * self.price
       
        #super(cart_detail, self).save(*args, **kwargs) 





ORDER_STATUS=(
    ('Recevied','Recevied'),
    ('Processed','Processed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered'),
)


class order(models.Model):
    odrder_code=models.CharField(_('odrder_code'),max_length=12,default=genirite_code)
    user=models.ForeignKey(User,verbose_name=_('order'),related_name='user_order',on_delete=models.SET_NULL,null=True,blank=True)
    order_status=models.CharField(_('order_status'),max_length=12,choices=ORDER_STATUS,default='Recevied')
    delivery_date=models.DateTimeField(_('delivery_date'),null=True,blank=True)
    order_date=models.DateTimeField(_('order_date'),default=timezone.now)

    def __str__(self):
        return self.odrder_code


class order_detail(models.Model):
    order=models.ForeignKey(order,verbose_name=_('order_detail'),related_name='odere_detail',on_delete=models.CASCADE)
    product=models.ForeignKey(product,verbose_name=_('product'),related_name='order_product',on_delete=models.SET_NULL,null=True,blank=True)
    price=models.FloatField(_('price'))
    quantity=models.IntegerField(_('quantity'), default=1)


    
    total=models.FloatField(_('total'),null=True,blank=True)





    def __str__(self):
        return str(self.order)


    def save(self, *args, **kwargs):
        self.total= self.quantity * self.price
       
        super(order_detail, self).save(*args, **kwargs) 





        

class Coupon(models.Model):
    code=models.CharField(max_length=20)
    from_date=models.DateField(default=timezone.now)
    to_date=models.DateField(default=timezone.now)
    quantity=models.IntegerField()
    value=models.FloatField()
    
    def __str__(self):
        return self.code