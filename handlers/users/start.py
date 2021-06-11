from aiogram import types

from loader import dp

from aiogram.dispatcher.filters import Command


@dp.message_handler(Command("start"))
async def bot_start(message: types.Message):
    await message.answer(f"Hi, {message.from_user.full_name}\n\n"
                         f"/help for more")


