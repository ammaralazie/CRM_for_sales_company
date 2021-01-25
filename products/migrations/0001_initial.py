# Generated by Django 3.1.5 on 2021-01-15 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRDName', models.CharField(max_length=300, verbose_name='name of product')),
                ('PRDName_ar', models.CharField(max_length=300, verbose_name='name of product')),
                ('PRDPrice', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='The price')),
                ('PRDPrice_ar', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='The price')),
                ('PRDDiscription', models.TextField()),
                ('PRDDiscription_ar', models.TextField()),
                ('PRDIamge', models.ImageField(default='/none.jpeg', upload_to='media')),
                ('PRDType', models.CharField(choices=[('Carpets and meridians', 'Carpets and meridians'), ('the games', 'the games'), ('Electrical', 'Electrical'), ('Mobile phones', 'Mobile phones')], max_length=90)),
                ('PRDType_ar', models.CharField(choices=[('سجادات و زوالي', 'سجادات و زوالي'), ('الالعاب', 'الالعاب'), ('الكهربائيات', 'الكهربائيات'), ('الهواتف المحمولة', 'الهواتف المحمولة')], max_length=90)),
                ('PRDSate', models.CharField(choices=[('new', 'new'), ('old', 'old')], max_length=20)),
                ('PRDSate_ar', models.CharField(choices=[('new', 'new'), ('old', 'old')], max_length=20)),
                ('PRDDiscount', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='The price')),
                ('PRDSlug', models.SlugField(blank=True, null=True)),
            ],
        ),
    ]
