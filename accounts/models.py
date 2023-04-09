from django.db import models
from django.contrib.auth.models import User
from orders.utils.genirite_code import genirite_code




class Profile(models.Model):
    user=models.OneToOneField(User,related_name='user_profile',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='profile/')
    code=models.CharField(max_length=20,default=genirite_code)


number_choices=(
    ('Primary','Primary'),
    ('Secondary','Secondary')
)


class ContactNumber(models.Model):
    user=models.ForeignKey(User,related_name='user_number',on_delete=models.CASCADE)
    typy=models.CharField(max_length=20,choices=number_choices)
    number=models.CharField(max_length=20)


adresse_choices=(
    ('Home','Home'),
    ('Office','Office'),
    ('Business','Business'),
    ('Acadmy','Acadmy'),
    ('Other','Other'),
)


class Adresse(models.Model):
    user=models.ForeignKey(User,related_name='user_adresse',on_delete=models.CASCADE)
    tybe=models.CharField(max_length=20,choices=adresse_choices)
    city=models.CharField(max_length=20)
    street=models.CharField(max_length=20)
    number=models.CharField(max_length=10)
    notes=models.CharField(max_length=20)
