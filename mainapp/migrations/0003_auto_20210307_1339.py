# Generated by Django 3.1.2 on 2021-03-07 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20210307_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='amount_of_discount',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=3, null=True, verbose_name='Размер скидки'),
        ),
        migrations.AddField(
            model_name='product',
            name='discount_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True, verbose_name='Цена по скидке'),
        ),
        migrations.AddField(
            model_name='product',
            name='sale',
            field=models.BooleanField(default=False, verbose_name='Наличие скидки'),
        ),
    ]
