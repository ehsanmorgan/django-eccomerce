from django.db import models

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=100)
    logo=models.ImageField(upload_to='company')
    call_us=models.CharField(max_length=20)
    email_us=models.EmailField(max_length=30)
    about=models.TextField(max_length=1000)
    fb_link=models.URLField(null=True,blank=True)
    insta_link=models.URLField(null=True,blank=True)
    tw_link=models.URLField(null=True,blank=True)
    goo_link=models.URLField(null=True,blank=True)


    emails=models.CharField(max_length=30)
    phonse=models.CharField(max_length=30)
    adresse=models.CharField(max_length=30)


    def __str__(self):
        return self.name


