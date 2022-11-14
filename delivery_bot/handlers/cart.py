from contextlib import suppress
from aiogram import types, Router, exceptions
from aiogram.fsm.context import FSMContext
from magic_filter import F

from repositories.open_api import api_io
from callback.menu import MenuCallbackFactory, ActionCallbackFactory
from keyboards.categories import get_keyboard_item
from keyboards.cart import get_keyboard_cart
from utils.cart import Cart
from utils.send import send_item
from states.order import Order
from utils.text import split_text
router = Router()


@router.callback_query(Order.choose_of_goods, MenuCallbackFactory.filter(F.action.in_({'up', 'down'})))
async def add_cart(c: types.CallbackQuery, state: FSMContext, callback_data: MenuCallbackFactory):
    data = await state.get_data()
    cart = Cart.loads(data=data.get('cart', None))
    if callback_data.action == 'up':
        if cart.len() >= 30:
            await c.answer('Не более 30 позиций в одном заказе', show_alert=True)
            return
        count = cart.add(
            (callback_data.item, callback_data.size), callback_data.price)
    else:
        count = cart.remove((callback_data.item, callback_data.size))

    await state.update_data({'cart': cart.dumps()})

    product = api_io.call_retrieveProducts(
        parameters={'id': callback_data.item})

    with suppress(exceptions.TelegramBadRequest):
        await c.message.edit_reply_markup(reply_markup=get_keyboard_item(product, cart))
    await c.answer(f'Итоговая сумма: {cart.get_total()}', show_alert=False)


@router.message(Order.choose_of_goods, F.text == '🧺Корзина')
async def view_cart(m: types.Message, state: FSMContext):
    data = await state.get_data()
    if 'cart' not in data:
        await m.reply('Корзина пуста')
        return
    await m.answer('считаем...')
    cart = Cart.loads(data['cart'])
    for item in split_text(cart.view()):
        await m.answer(item, reply_markup=get_keyboard_cart())


@router.callback_query(Order.choose_of_goods, ActionCallbackFactory.filter(F.action == 'edit'))
async def edit_cart(c: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if 'cart' not in data:
        await c.message.reply('Корзина пуста')
        await c.answer()
        return
    cart = Cart.loads(data['cart'])
    sent = []
    for item in cart.items:
        if item[0] in sent:
            continue
        sent.append(item[0])
        product = api_io.call_retrieveProducts(parameters={'id': item[0]})
        await send_item(c.message, product, cart, edit=True)
    await c.message.answer(f'Итоговая сумма: {cart.get_total()}')
    await c.answer()


@router.callback_query(Order.choose_of_goods, ActionCallbackFactory.filter(F.action == 'erase'))
async def erase_cart(c: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if 'cart' in data:
        data.pop('cart')
    await state.set_data(data)
    await c.answer('Корзина очищена')
