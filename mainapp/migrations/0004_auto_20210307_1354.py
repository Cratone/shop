# Generated by Django 3.1.2 on 2021-03-07 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20210307_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sale',
            field=models.BooleanField(default=True, verbose_name='Наличие скидки'),
        ),
    ]
