# Generated by Django 3.1.5 on 2021-01-15 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210115_0542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='PRDDiscount_ar',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='The price in arabic'),
        ),
    ]
