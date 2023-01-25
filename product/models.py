from django.db import models
from taggit.managers import TaggableManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify



# Create your models here.
Flag_product={
    ('Sale','Sales'),
    ('Feature','Feature'),
    ('New','New')
}

class product(models.Model):

    name=models.CharField(_('name'),  max_length=20)
    flag=models.CharField(_('flag'),max_length=20,choices=Flag_product)
    image=models.ImageField(_('image'), upload_to='products/',default='default.png')
    price=models.FloatField(_('price'),)
    sku=models.IntegerField(_('sku'),)
    brand=models.ForeignKey('Brand',verbose_name=_('brand'), related_name='product_name',on_delete=models.CASCADE)
    tags=TaggableManager()
    subtitle=models.TextField(_('subtitle'),max_length=500)
    description=models.TextField(_('description'), max_length=1000)
    slug=models.SlugField(null=True,blank=True)



    def save(self,*args, **kwargs):
        self.slug=self.name
        super(product,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

    
class product_image(models.Model):
    product=models.ForeignKey(product,verbose_name=_('product'), related_name='product_image',on_delete=models.CASCADE)
    image=models.ImageField( _('image'), upload_to='product_images/')
    def __str__(self):
        return str(self.product)




class Brand(models.Model):
    name=models.CharField(_('brand'), max_length=100)
    image=models.ImageField( _('image'), upload_to='brand/')

    def __str__(self):
        return self.name


class reviews(models.Model):
    user=models.ForeignKey(User,verbose_name=_('reviews'), related_name='review_author',on_delete=models.SET_NULL,null=True,blank=True)
    product=models.ForeignKey(product,verbose_name=_('product'), related_name='product_review',on_delete=models.CASCADE)
    comment=models.CharField(_('comment'), max_length=300)
    rate=models.IntegerField(_('rate'))
    createt_at=models.DateTimeField(_('createt_at'), default=timezone.now)

    def __str__(self):
        return str(self.product)
