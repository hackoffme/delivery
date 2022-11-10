import logging
from os import getenv
from aiohttp.web import run_app
from aiohttp.web_app import Application

from aiogram import Bot, Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiogram.fsm.storage.redis import Redis, RedisStorage

from handlers import other, start, menu, cart, order, history, about
from middleware.worktime import WorkTime


TELEGRAM_TOKEN = getenv("TOKEN")
APP_BASE_URL = getenv("APP_BASE_URL")


async def on_startup(bot: Bot, base_url: str):
    await bot.set_webhook(f"{base_url}/bot")

async def on_shutdown(dispatcher: Dispatcher, bot: Bot):
    await bot.delete_webhook()

def register_dp():
    # dp = Dispatcher(storage=RedisStorage())
    dp = Dispatcher(storage=RedisStorage.from_url(url='redis://redis:6379/db'))
    dp["base_url"] = APP_BASE_URL
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    dp.include_router(start.router)
    dp.include_router(menu.router)
    dp.include_router(cart.router)
    order.router.message.middleware(WorkTime())
    order.router.callback_query.middleware(WorkTime())
    dp.include_router(order.router)
    dp.include_router(history.router)
    dp.include_router(about.router)
    dp.include_router(other.router)
    return dp

def main():
    bot = Bot(token=TELEGRAM_TOKEN, parse_mode="HTML")
    dp = register_dp()
    app = Application()
    app["bot"] = bot

    SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
    ).register(app, path="/webhook")
    
    setup_application(app, dp, bot=bot)

    run_app(app, host="bot", port=3001)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()