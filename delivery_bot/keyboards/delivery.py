from aiogram import types

from callback.menu import ActionCallbackFactory


# def get_keyboard_addres():
#     kb = types.InlineKeyboardMarkup(inline_keyboard=[
#         [types.InlineKeyboardButton(text='Ввести адрес',
#                                     callback_data=ActionCallbackFactory(action='adr').pack()),
#          types.InlineKeyboardButton(text='Отправить геолокацию',
#                                     callback_data=ActionCallbackFactory(action='geo').pack())],
#         [types.InlineKeyboardButton(text='Вернуться к выбору еды',
#                                     callback_data=ActionCallbackFactory(action='back').pack())]
#     ])
#     return kb

def get_keyboard_confirm_order():
    kb = types.InlineKeyboardMarkup(inline_keyboard=[
        [types.InlineKeyboardButton(text='🏡Редактировать адрес',
                                    callback_data=ActionCallbackFactory(action='eadr').pack()),
         types.InlineKeyboardButton(text='📋Редактировать заказ',
                                    callback_data=ActionCallbackFactory(action='edit').pack())],
        [types.InlineKeyboardButton(text='👉Подтвердить заказ👈',
                                    callback_data=ActionCallbackFactory(action='conf').pack())]
    ])
    return kb

def get_keyboard_phone():
    kb = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text='Отправьте свой контакт',  request_contact=True)]],
                                resize_keyboard=True, one_time_keyboard=True)
    return kb