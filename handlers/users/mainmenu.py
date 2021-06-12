from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import dp

from aiogram.dispatcher.filters import Command

from keyboards.default import menu


@dp.message_handler(Command("menu"))
async def bot_help(message: types.Message):
    await message.answer("Menu", reply_markup=menu)
