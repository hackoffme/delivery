import logging
from aiogram import Bot, Dispatcher

from config import settings
from handlers import other, start, menu, cart, order, history, about
from middleware.worktime import WorkTime

logger = logging.getLogger(__name__)


def main() -> None:
    bot = Bot(settings.token, parse_mode="HTML")
    dp = Dispatcher()
    dp.include_router(start.router)
    dp.include_router(menu.router)
    dp.include_router(cart.router)
    order.router.message.middleware(WorkTime())
    order.router.callback_query.middleware(WorkTime())
    dp.include_router(order.router)
    dp.include_router(history.router)
    dp.include_router(about.router)

    dp.include_router(other.router)
    dp.run_polling(bot)


if __name__ == "__main__":
    main()
