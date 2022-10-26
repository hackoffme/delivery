from aiogram import types

allowed_commands = ['📋меню', '🧺корзина', '📜история', '🍕о нас']

def get_keyboard_start():
    buttons = [
        [
            types.KeyboardButton(text='📋Меню'),
            types.KeyboardButton(text='🧺Корзина')
        ],
        [
            types.KeyboardButton(text='📜История'),
            types.KeyboardButton(text='🍕О нас'),
        ]
        
    ]
    return types.ReplyKeyboardMarkup(keyboard=buttons,
                                     resize_keyboard=True, 
                                     input_field_placeholder='Нажмите меню 📋')