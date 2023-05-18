

import os,django
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
django.setup()

from faker import Faker
import random
from product.models import product as Product ,Brand,reviews
from django.contrib.auth.models import User


def seed_brand(n):
    fake=Faker()
    images=['apple.png','Download.jpeg','images_1.jpeg','images_2.jpeg','images_3.jpeg','images_4.jpeg','images_5.jpeg','images_6.jpeg','images_7.jpeg','images.jpeg','samsung.png']

    for _ in range(n):
        name = fake.name()
        image=f"brand/{images[random.randint(0,10)]}"
        Brand.objects.create(name=name,image=image)

    print(f"seed{n} Brands ...")





def seed_product(n):
    Flag_product=['Sale','Feature','New']
    fake=Faker()
    images=[ 'huawei.jpeg','Download_2.jpeg','Download.jpeg','3.jpeg','images.jpeg','4.jpeg','5.jpeg','6.jpeg','7.jpeg','8.jpeg','9.jpeg','10.jpeg','11.jpeg','12.jpeg','13.jpeg','14.jpeg','15.jpeg','16.jpeg','17.jpeg','18.jpeg','19.jpeg','20.jpeg','21.jpeg','22.jpeg']
    for _ in range(n):
        image=f"products/{images[random.randint(0,23)]}"
        name=fake.name()
        brand=Brand.objects.get(id=random.randint(504,528))
        flag=Flag_product[random.randint(0,2)]
        subtitle=fake.text(max_nb_chars=(500))
        quantity=random.randint(2,30)
        sku=random.randint(1,10000)
        description=fake.text(max_nb_chars=(1000))
        price=round(random.uniform(400.99,999.99),2)

        Product.objects.create(
            image=image,
            name=name,
            brand=brand,
            flag=flag,
            subtitle=subtitle,
            quantity=quantity,
            sku=sku,
            description=description,
            price=price

        )

    print(f"seed{n} products ...")


def seed_comment(n):
    fake=Faker()
    for _ in range(n) :
        comment=fake.text(max_nb_chars=20)
        rate=random.randint(1,6)
        product=Product.objects.get(id=random.randint(3300,5000))
        
        reviews.objects.create(
            comment=comment,
            rate=rate,
            product=product
            
        )
        
    print(f"Seed{n} Comment ...")





seed_brand(20)
seed_product(1000)
seed_comment(300)
