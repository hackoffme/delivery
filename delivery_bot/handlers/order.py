import dataclasses
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram import Router
from aiogram import html
from magic_filter import F
from openapi3.errors import UnexpectedResponseError

from callback.menu import ActionCallbackFactory
from states.order import Order
from repositories.open_api import api_io
from keyboards.delivery import get_keyboard_phone, get_keyboard_confirm_order
from keyboards.start import get_keyboard_start, allowed_commands
from utils.cart import Cart
from utils.models import User
from utils.text import split_text

router = Router()


@router.callback_query(Order.choose_of_goods, ActionCallbackFactory.filter(F.action == 'by'))
async def by(c: types.CallbackQuery, state: FSMContext, callback_data: ActionCallbackFactory):
    try:
        user = api_io.call_retrieveCustomerTg(
            parameters={'tg_id': c.from_user.id})
        user = User(tg_id=user.tg_id, address=user.address, phone=user.phone)
        await state.update_data({'user': dataclasses.asdict(user)})
    except UnexpectedResponseError:
        await state.set_state(Order.set_address)
        await c.message.answer('Введите адрес')
        return
    await c.answer()
    await confirmation_order(c.message, user, state)


@router.message(Order.set_address, content_types='text')
async def get_address(m: types.Message, state: FSMContext):
    if m.text.lower() in allowed_commands:
        await m.answer('Отправьте адрес сообщением')
        return
    await state.update_data({'address': html.quote(m.text)})
    await m.answer('Нажмите кнопку поделиться телефоном', reply_markup=get_keyboard_phone())
    await state.set_state(Order.choose_of_goods)
    await state.set_state(Order.set_phone)


@router.message(Order.set_phone, content_types='contact')
async def get_phone(m: types.Message, state: FSMContext):
    data = await state.get_data()
    q = {
        "tg_id": m.from_user.id,
        "address": data['address'],
        "phone": m.contact.phone_number
    }
    try:
        user = api_io.call_createCustomerTg(data=q)
    except UnexpectedResponseError:
        user = api_io.call_updateCustomerTg(
            parameters={'tg_id': m.from_user.id}, data=q)
    user = User(tg_id=user.tg_id, address=user.address, phone=user.phone)
    await state.update_data({'user': dataclasses.asdict(user)})
    await m.answer('Адрес и телефон сохранены', reply_markup=get_keyboard_start())
    await state.set_state(Order.choose_of_goods)
    await confirmation_order(m, user, state)


@router.callback_query(ActionCallbackFactory.filter(F.action == 'eadr'))
async def edit_address(c: types.CallbackQuery, state: FSMContext):
    await state.set_state(Order.set_address)
    await c.message.answer('Введите адрес')
    await c.answer()


async def confirmation_order(m: types.Message, user, state: FSMContext):
    cart = Cart.loads((await state.get_data()).get('cart', None))
    if not cart.items:
        await m.answer('Ошибка формирования заказа, корзина пуста. Попробуйте еще раз')
        return
    if not user:
        await m.answer('Ошибка получения данных пользователя. Заполните еще раз адрес и имя')
        return
    ret = f'Ваш адрес: {user.address}\nВаш телефон: {user.phone}\n{cart.view()}'
    for item in split_text(ret):
        await m.answer(item, reply_markup=get_keyboard_confirm_order())


@router.callback_query(ActionCallbackFactory.filter(F.action == 'conf'))
async def confirmed_order(c: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user = User(**data.get('user'))
    items: Cart = Cart.loads(data.get('cart'))

    if not items.items:
        await c.message.answer('Ошибка формирования заказа, корзина пуста. Добавьте товар в корзину')
        return
    if not user:
        await c.message.answer('Ошибка получения данных пользователя. Заполните еще раз адрес и имя')
        return

    order = {
        "customer": user.tg_id,
        "items": items.data_for_send()
    }
    try:
        ret = api_io.call_createOrderCreate(data=order)
        await c.message.answer('Ваш заказ поступил в обработку. Ожидайте звонка менеджера')
        await state.set_data({})
    except:
        await c.message.answer('Проблема с отправкой заказа. Попробуйте еще или позвоните нам')
    finally:
        await state.set_state(state=Order.choose_of_goods)

    await c.answer()
