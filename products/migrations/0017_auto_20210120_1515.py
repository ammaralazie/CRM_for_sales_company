# Generated by Django 3.1.5 on 2021-01-20 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20210120_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='phone_number2',
            field=models.CharField(default='', max_length=11),
            preserve_default=False,
        ),
    ]
