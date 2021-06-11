from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import dp

from aiogram.dispatcher.filters import Command


@dp.message_handler(Command("menu"))
async def bot_help(message: types.Message):
    menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Show Bitcoin price \U0001f4b0"),
            ],
            [
                KeyboardButton(text="Take a test \U0001f4dd"),
                KeyboardButton(text="Order own bot \U0001F916"),
            ],
            [
                KeyboardButton(text="New button"),
            ],
        ], resize_keyboard=True
    )
    await message.answer("Menu", reply_markup=menu)
