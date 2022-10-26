from aiogram import Router
from aiogram import types
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from magic_filter import F


from keyboards import start
from states.order import Order

router = Router()

@router.message(Order.choose_of_goods, F.text == '🍕О нас')
async def about(message: types.Message, state: FSMContext):
    await message.answer(text='Информация о нас')