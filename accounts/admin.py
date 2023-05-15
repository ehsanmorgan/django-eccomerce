from django.contrib import admin
from .models import Adresse,Profile,ContactNumber

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display=['user']
    



admin.site.register(Profile,ProfileAdmin)
admin.site.register(ContactNumber)
admin.site.register(Adresse)




