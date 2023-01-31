from django.db import models
from django.utils import timezone
from product.models import product
from django.contrib.auth.models import User
from .utils.genirite_code import genirite_code

# Create your models here.

ORDER_STATUS=(
    ('Recevied','Recevied'),
    ('Processed','Processed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered'),
)


class order(models.Model):
    odrder_code=models.CharField(max_length=10,default=genirite_code)
    user=models.ForeignKey(User,related_name='user_order',on_delete=models.SET_NULL,null=True,blank=True)
    order_status=models.CharField(max_length=12,choices=ORDER_STATUS,default='Recevied')
    delivery_date=models.DateTimeField(null=True,blank=True)
    order_date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.odrder_code


class order_detail(models.Model):
    order=models.ForeignKey(order,related_name='odere_detail',on_delete=models.CASCADE)
    product=models.ForeignKey(product,related_name='order_product',on_delete=models.SET_NULL,null=True,blank=True)
    price=models.FloatField()
    quantity=models.IntegerField(default=1)
    total=models.FloatField(null=True,blank=True)





    def __str__(self):
        return str(self.order)


    def save(self, *args, **kwargs):
        self.total= self.quantity * self.price
       
        super(order_detail, self).save(*args, **kwargs) 

    

