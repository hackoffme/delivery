from aiogram import Router
from aiogram import types
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

from keyboards import start
from states.order import Order
from utils.text import hi

router = Router()


@router.message(Command(commands=['start']))
async def cmd_start(message: types.Message, state: FSMContext):
    await message.answer(text=hi, reply_markup=start.get_keyboard_start())
    await state.set_state(Order.choose_of_goods)
