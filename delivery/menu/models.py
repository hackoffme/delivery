import io
import os
from django.db import models
from django.core.files.base import ContentFile
from django.db.models.fields.files import ImageFieldFile
from PIL import Image


class Base(models.Model):
    class Meta:
        abstract = True


class Categories(Base):
    name = models.CharField(max_length=200, verbose_name='Категория')
    emoji = models.CharField(max_length=2, blank=True, null=True, verbose_name='Эмодзи')
    slug = models.SlugField(max_length=200, unique=True, db_index=True, verbose_name='slug')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
        
class WEBPFieldFile(ImageFieldFile):
    def save(self, name, content, save=True):
        content.file.seek(0)
        image = Image.open(content.file)
        image_bytes = io.BytesIO()
        
        fixed_width = 900
        height_size = int(image.size[1] * fixed_width / float(image.size[0]))
        image = image.resize((fixed_width, height_size))
        
        image.save(fp=image_bytes, format="WEBP")
        image_content_file = ContentFile(content=image_bytes.getvalue())

        name = os.path.splitext(name)[0]+'.webp'
        super().save(name, image_content_file, save)
 
 
class WEBPField(models.ImageField):
    attr_class = WEBPFieldFile
    

class Products(Base):
    name = models.CharField(max_length=200,
                            verbose_name='Название блюда')
    slug = models.SlugField(max_length=200,
                            unique=True,
                            db_index=True,
                            verbose_name='slug')
    category = models.ForeignKey(Categories,
                                 on_delete=models.CASCADE,
                                 related_name='products',
                                 verbose_name='Категория')
    description = models.TextField(blank=True,
                                   verbose_name='Описание')
    image = WEBPField(upload_to='media/img/%Y/%m',
                              null=True,
                              blank=True,
                              verbose_name='Фотография')
    aviable = models.BooleanField(default=True,
                                  db_index=True,
                                  verbose_name='Доступно для заказа')
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Меню'
        index_together = [
            ['category', 'aviable']
        ]


class Price(Base):
    product = models.ForeignKey(Products,
                                on_delete=models.CASCADE,
                                db_index=True,
                                related_name='price',
                                verbose_name='Продукт')
    slug = models.SlugField(max_length=200,
                            unique=True,
                            db_index=True,
                            verbose_name='slug')
    size = models.CharField(max_length=30, db_index=True, verbose_name='Размер блюбда')
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                verbose_name='Цена')

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'
        index_together = [
            ['product', 'size']
        ]

    def __str__(self):
        return f'{self.product.name}>>{self.size}>>{self.price}'

