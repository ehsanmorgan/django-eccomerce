# Generated by Django 4.1.5 on 2023-05-16 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0026_alter_product_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='flag',
            field=models.CharField(choices=[('Feature', 'Feature'), ('New', 'New'), ('Sale', 'Sales')], max_length=20, verbose_name='flag'),
        ),
    ]
