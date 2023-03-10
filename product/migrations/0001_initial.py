# Generated by Django 4.1.5 on 2023-01-24 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='brand')),
                ('image', models.ImageField(upload_to='brand/', verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='name')),
                ('flag', models.CharField(choices=[('New', 'New'), ('Sale', 'Sales'), ('Feature', 'Feature')], max_length=20, verbose_name='flag')),
                ('image', models.ImageField(default='default.png', upload_to='products/', verbose_name='image')),
                ('price', models.FloatField(verbose_name='price')),
                ('sku', models.IntegerField(verbose_name='sku')),
                ('subtitle', models.TextField(max_length=500, verbose_name='subtitle')),
                ('description', models.TextField(max_length=1000, verbose_name='description')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_name', to='product.brand', verbose_name='brand')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=300, verbose_name='comment')),
                ('rate', models.IntegerField(verbose_name='rate')),
                ('createt_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='createt_at')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_review', to='product.product', verbose_name='product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='review_author', to=settings.AUTH_USER_MODEL, verbose_name='reviews')),
            ],
        ),
        migrations.CreateModel(
            name='product_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images/', verbose_name='image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='product.product', verbose_name='product')),
            ],
        ),
    ]
