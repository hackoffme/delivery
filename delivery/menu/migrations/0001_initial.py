# Generated by Django 4.1.1 on 2022-10-21 09:09

from django.db import migrations, models
import django.db.models.deletion
import menu.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Категория')),
                ('emoji', models.CharField(blank=True, max_length=2, null=True, verbose_name='Эмодзи')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название блюда')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='slug')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('image', menu.models.WEBPField(blank=True, null=True, upload_to='media/img/%Y/%m', verbose_name='Фотография')),
                ('aviable', models.BooleanField(default=True, verbose_name='Доступно для заказа')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='menu.categories', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Блюдо',
                'verbose_name_plural': 'Меню',
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='slug')),
                ('size', models.CharField(max_length=30, verbose_name='Размер блюбда')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='price', to='menu.products', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Цена',
                'verbose_name_plural': 'Цены',
            },
        ),
    ]
