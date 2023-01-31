# Generated by Django 4.1.5 on 2023-01-31 17:44

from django.db import migrations, models
import orders.utils.genirite_code


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_rename_totla_order_detail_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='odrder_code',
            field=models.CharField(default=orders.utils.genirite_code.genirite_code, max_length=12),
        ),
        migrations.AlterField(
            model_name='order_detail',
            name='total',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
