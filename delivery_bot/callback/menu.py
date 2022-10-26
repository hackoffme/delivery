from aiogram.filters.callback_data import CallbackData

class MenuCallbackFactory(CallbackData, prefix='m'):
    category: int | None
    item: int | None
    size: int | None
    action: str | None
    price: int | None
    
class ActionCallbackFactory(CallbackData, prefix='a'):
    action: str | None
