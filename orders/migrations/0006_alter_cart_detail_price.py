# Generated by Django 4.1.5 on 2023-03-14 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_cart_cart_status_alter_cart_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_detail',
            name='price',
            field=models.FloatField(blank=True, null=True, verbose_name='price'),
        ),
    ]
