from aiogram import types, Router
from aiogram.filters.command import Command
from magic_filter import F

from keyboards.categories import get_keyboard_categories
from callback.menu import MenuCallbackFactory
from repositories import api_io
from utils.send import send_item
from states.order import Order

router = Router()

@router.message(Order.choose_of_goods, F.text=='📋Меню')
async def menu(m: types.Message):
    await m.answer('Меню', reply_markup=get_keyboard_categories().as_markup())


@router.callback_query(Order.choose_of_goods, MenuCallbackFactory.filter((F.category!=None) & (F.item == None)))
async def category(c: types.CallbackQuery, callback_data: MenuCallbackFactory):
    menu = api_io.call_listProductsSerializers(parameters={'id': callback_data.category})
    await c.answer()
    for item in menu:
        await send_item(c.message, item)

