# Generated by Django 3.1.5 on 2021-01-18 11:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_address_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='date_add',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
