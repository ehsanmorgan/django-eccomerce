# Generated by Django 4.1.5 on 2023-05-17 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0031_alter_product_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='flag',
            field=models.CharField(choices=[('Sale', 'Sales'), ('New', 'New'), ('Feature', 'Feature')], max_length=20, verbose_name='flag'),
        ),
    ]