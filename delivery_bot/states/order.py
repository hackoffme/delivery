from aiogram.fsm.state import State, StatesGroup


class Order(StatesGroup):
    choose_of_goods = State()
    set_address = State()
    set_phone = State()
