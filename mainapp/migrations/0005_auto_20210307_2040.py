# Generated by Django 3.1.2 on 2021-03-07 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0004_auto_20210307_1354'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст отзыва')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор отзыва')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_comment', to='mainapp.product', verbose_name='Товар')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='related_product', to='mainapp.Comment', verbose_name='Комментарии'),
        ),
    ]
