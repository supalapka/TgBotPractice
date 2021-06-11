from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp



# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(f"Sorry, I do not understand.\n"
                         f"Message:\n"
                         f"{message.text}")

