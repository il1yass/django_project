# Generated by Django 4.2.6 on 2023-10-28 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='URL')),
                ('price', models.TextField(blank=True, verbose_name='Цена')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Изображение')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
            ],
            options={
                'verbose_name': 'Товары',
                'verbose_name_plural': 'Товары',
                'ordering': ['time_create', 'title'],
            },
        ),
    ]
