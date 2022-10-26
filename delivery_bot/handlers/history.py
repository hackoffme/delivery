from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from magic_filter import F
import json
from repositories import api_io
from utils.order_to_text import order_to_text
from states.order import Order
router = Router()

@router.message(Order.choose_of_goods, F.text=='📜История')
async def history(m: types.Message, state: FSMContext):
    data = api_io.call_listOrderViews(parameters={'tg_id':m.from_user.id})
    if not data:
        await m.answer('История заказов пуста')
        return
    for item in data:
        # order_text = order_to_text(item)
        await m.answer(item.view)
    
