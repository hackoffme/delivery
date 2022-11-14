from typing import Callable, Dict, Any, Awaitable
from datetime import datetime
from aiogram.types import TelegramObject
from aiogram import BaseMiddleware

from config import settings


def work_time():
    current_time = datetime.now().time()
    return settings.time_start < current_time and settings.time_end > current_time


class WorkTime(BaseMiddleware):
    async def __call__(self,
                       handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
                       event: TelegramObject,
                       data: Dict[str, Any]) -> Any:
        if work_time():
            result = await handler(event, data)
            return result

        await event.answer(
            f'Время работы с {settings.time_start} по {settings.time_end}',
            show_alert=True
        )
        return
