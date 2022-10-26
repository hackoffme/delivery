from aiogram import types

from callback.menu import ActionCallbackFactory


def get_keyboard_cart():
    kb = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text='🧹Очистить',
                                    callback_data=ActionCallbackFactory(action='erase').pack()),
         types.InlineKeyboardButton(text='📋Редактировать',
                                    callback_data=ActionCallbackFactory(action='edit').pack())],
        [types.InlineKeyboardButton(text='👉Оформить👈',
                                    callback_data=ActionCallbackFactory(action='by').pack())]
    ])
    return kb
