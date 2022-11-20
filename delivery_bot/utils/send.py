from contextlib import suppress
from aiogram import types, exceptions

from keyboards.categories import get_keyboard_item
from utils.cached_photo import cache_photo
import logging

logger = logging.getLogger(__name__)

async def send_item(m: types.Message, data, basket=None, edit=False):
    caption = f"<b>{data.name}</b>\n " \
              f"<code>{data.description}</code>"
    kb = get_keyboard_item(data, basket)

    if data.image and not edit:
        # logger.info(data.image)
        photo = cache_photo.get(data.image)
        if photo:
            with suppress(exceptions.TelegramBadRequest):
                r = await m.answer_photo(cache_photo.get(data.image),
                                         caption=caption, reply_markup=kb)

                cache_photo.update(data.image, r.photo[-1].file_id)
            return
    await m.answer(caption, reply_markup=kb)
