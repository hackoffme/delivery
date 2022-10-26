from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram import Router
from magic_filter import F

from keyboards.start import allowed_commands

router = Router()

@router.message(F.text.lower().in_(allowed_commands))
async def all_command(m: types.Message, state: FSMContext):
    s = await state.get_state()
    if not await state.get_state():
        await m.answer('Нажмите на /start')
    
    