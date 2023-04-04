from .models import product
from modeltranslation.translator import TranslationOptions ,translator

class ProductTranslationOptions(TranslationOptions):
    fields = ( 'flag' ,'description','brand','price')
    
    
    
translator.register(product,ProductTranslationOptions)
