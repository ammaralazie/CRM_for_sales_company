# Generated by Django 3.1.5 on 2021-01-19 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210118_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='covernorate',
            field=models.CharField(default='بغداد', max_length=30),
        ),
        migrations.RemoveField(
            model_name='address',
            name='order',
        ),
        migrations.AddField(
            model_name='address',
            name='order',
            field=models.ManyToManyField(to='products.OrderItem'),
        ),
    ]
