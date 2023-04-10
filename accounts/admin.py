from django.contrib import admin
from .models import Adresse,Profile,ContactNumber

# Register your models here.

admin.site.register(Profile)
admin.site.register(ContactNumber)
admin.site.register(Adresse)

