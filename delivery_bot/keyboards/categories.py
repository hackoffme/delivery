from aiogram.utils.keyboard import InlineKeyboardBuilder

from repositories.open_api import api_io
from callback.menu import MenuCallbackFactory


def get_keyboard_categories():
    builder = InlineKeyboardBuilder()
    q = api_io.call_listCategories()
    for item in q:
        builder.button(
            text=item.name + (item.emoji or ''),
            callback_data=MenuCallbackFactory(category=item.id)
        )
    builder.adjust(1)
    return builder


def get_keyboard_item(data, basket=None):
    builder = InlineKeyboardBuilder()
    for item in data.price:
        count = 0
        if basket and (data.id, item.id) in basket.items.keys():
            count = basket.items[(data.id, item.id)]

        message = f'Цена: {int(item.price)} | Вес: {item.size}'
        if count:
            message = f'Кол-во {count} {message}'
        builder.button(text=message,
                       callback_data='empty')
        builder.button(text='❌ ',
                       callback_data=MenuCallbackFactory(category=data.category,
                                                         item=data.id,
                                                         size=item.id,
                                                         price=item.price,
                                                         action='down'))
        builder.button(text='✅ ',
                       callback_data=MenuCallbackFactory(category=data.category,
                                                         item=data.id,
                                                         size=item.id,
                                                         price=item.price,
                                                         action='up'))
    builder.adjust(1, 2, repeat=True)
    return builder.as_markup()
