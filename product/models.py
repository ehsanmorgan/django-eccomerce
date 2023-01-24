from django.db import models
from taggit.managers import TaggableManager
from django.utils.translation import gettext_lazy as _



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
    
    def __str__(self):
        return self.name
class product_image(models.Model):
    pass
    '''
    product:foreginkey
    image
    '''


class Brand(models.Model):
    pass


class reviews(models.Model):
    pass