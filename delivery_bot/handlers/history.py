from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from magic_filter import F

from repositories import api_io
from states.order import Order
from utils.text import split_text
router = Router()


@router.message(Order.choose_of_goods, F.text == '📜История')
async def history(m: types.Message, state: FSMContext):
    data = api_io.call_listOrderViews(parameters={'tg_id': m.from_user.id})
    if not data:
        await m.answer('История заказов пуста')
        return
    for item in data:
        for t in split_text(item.view):
            await m.answer(t)
