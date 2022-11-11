from phone_field import PhoneField

from django.db import models
from menu.models import Base, Products, Price

class CustomersTg(Base):
    tg_id = models.IntegerField(unique=True,
                                db_index=True,
                                verbose_name='ID пользователя telegram')
    address = models.CharField(max_length=250,
                               verbose_name='Адрес доставки')
    phone = PhoneField(verbose_name='Номер телефона')

    class Meta:
        verbose_name = 'Пользователь телеграмм'
        verbose_name_plural = 'Пользователи телеграмм'
    def __str__(self) -> str:
        return f'id:{self.tg_id} телефон {self.phone}'


class OrderItems(Base):
    item = models.ForeignKey(Price,
                             on_delete=models.PROTECT,
                             verbose_name='Продукт')
    order = models.ForeignKey('Orders',
                             related_name='items',
                              on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='Количество')
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                verbose_name='Цена')
    def save(self, *args, **kwargs):
        if not self.price:
            self.price = self.item.price
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Содержимое заказа'
        verbose_name_plural = 'Содержимое заказов'


class Orders(Base):
    customer = models.ForeignKey(CustomersTg,
                                 on_delete=models.CASCADE,
                                 db_index=True,
                                 verbose_name='Заказчик')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Создание')
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name='Обновление')
    
    def total(self):
        total=0
        for item in self.items.all():
            total += item.item.price * item.quantity
        return total
    
    
    def view(self):
        price = ''
        total = 0
        for item in self.items.all():
            price += f'{item.item.product.name} {item.item.size} {item.quantity}x{item.item.price}\n'
            total += item.item.price * item.quantity

        return f'<b>Заказ</b> от {self.created.date()}\n'\
               f'<b>Адрес:</b> {self.customer.address}\n'\
               f'<b>Телефон:</b> {self.customer.phone}\n'\
               f'<b>Меню:</b> \n'\
               f'{price}'\
               f'<b>Итого: {total}</b>'

        
    def __str__(self):
        return f'Заказ №{self.id}'
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
