# Generated by Django 4.1.5 on 2023-07-16 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0033_alter_product_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='flag',
            field=models.CharField(choices=[('New', 'New'), ('Feature', 'Feature'), ('Sale', 'Sales')], max_length=20, verbose_name='flag'),
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wished_item', models.CharField(max_length=20)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wishlist_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
