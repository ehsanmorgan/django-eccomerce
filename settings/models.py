from django.db import models

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=100)
    logo=models.ImageField(upload_to='company')
    about=models.TextField(max_length=1000)
    emails=models.CharField(max_length=30)
    phonse=models.CharField(max_length=30)
    adresse=models.CharField(max_length=30)
    image=models.ImageField(default='default.png')






    def __str__(self):
        return self.name


